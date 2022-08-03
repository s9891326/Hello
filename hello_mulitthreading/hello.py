import threading
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests
import time


def first():
    def scraper(x):
        print("start")
        time.sleep(x)
        print("sleep done")
    
    t = threading.Thread(target=scraper, args=(1,))  # 建立執行緒
    print("t start")
    t.start()  # 執行
    print("end")


def scrape(urls):
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # 爬取文章標題
        titles = soup.find_all("h3", {"class": "post_title"})
        
        for title in titles:
            print(title.getText().strip())
            # title.getText().strip()
        
        time.sleep(1)
    return str(threading.get_ident())


# 爬取文章標題
base_url = "https://www.inside.com.tw/tag/AI"
urls = [f"{base_url}?page={page}" for page in range(1, 6)]  # 1~5頁的網址清單


def second():
    start_time = time.time()  # 開始時間
    scrape(urls)
    
    end_time = time.time()
    print(f"{end_time - start_time} 爬取 {len(urls)} 頁的文章")


def third():
    start_time = time.time()  # 開始時間
    
    # 同時建立及啟用10個執行緒
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(scrape, urls)
    # with ThreadPoolExecutor() as executor:  # 改用 with...as
    #     executor.submit(scrape, urls)
    #     executor.submit(scrape, urls)
    
    end_time = time.time()
    print(f"{end_time - start_time} 秒爬取 {len(urls)} 頁的文章")


def foo(bars):
    for bar in bars:
        print('hello {}'.format(bar))
        time.sleep(2)
    return 'foo'


def four():
    bars = range(10)
    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.map(foo, bars)
        return_value = future.result()
        print(return_value)


def change_use_threading():
    start_time = time.time()  # 開始時間
    
    # 同時建立及啟用5個執行緒
    workers = 5
    thread_list = []
    for i in range(workers):
        thread_list.append(threading.Thread(target=scrape, args=([urls[i]],)))
        thread_list[i].start()
    
    for thread in thread_list:
        thread.join()
    
    end_time = time.time()
    print(f"{end_time - start_time} 秒爬取 {len(urls)} 頁的文章")

if __name__ == '__main__':
    # first()
    # second()
    # third()
    # four()
    change_use_threading()

# 對CPU密集型程式碼(比如迴圈計算) - multiprocess效率更高
# 對IO密集型程式碼(比如檔案操作，網路爬蟲) - multithread效率更高。
# 對於IO密集型操作，大部分消耗時間其實是等待時間，在等待時間中CPU是不需要工作的，那你在此期間提供雙CPU資源也是利用不上的，相反對於CPU密集型程式碼，2個CPU幹活肯定比一個CPU快很多。那麼為什麼多執行緒會對IO密集型程式碼有用呢？這時因為python碰到等待會釋放GIL供新的執行緒使用，實現了執行緒間的切換。
# https://codychen.me/2019/12/%E5%A4%9A%E9%80%B2%E7%A8%8B/%E5%A4%9A%E5%9F%B7%E8%A1%8C%E7%B7%92-%E4%B8%A6%E7%99%BC/%E5%B9%B3%E8%A1%8C/

# https://stackoverflow.com/questions/27435284/multiprocessing-vs-multithreading-vs-asyncio-in-python-3
# if io_bound:
#     if io_very_slow:
#         print("Use Asyncio")
#     else:
#         print("Use Threads")
# else:
#     print("Multi Processing")
# CPU Bound => Multi Processing
# I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading
# I/O Bound, Slow I/O, Many connections => Asyncio
