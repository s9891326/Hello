import requests
import re

# base_url = "https://www.bilibili.com/video/av6499012"
# base_url = "https://service.ebook.hyread.com.tw/ebookservice/epubreader/hyread/v3/reader.jsp"
# base_url = "https://tnml.ebook.hyread.com.tw/index.jsp"
# base_url = "https://tnml.ebook.hyread.com.tw/bookDetail.jsp?id=237812"
base_url = "https://service.ebook.hyread.com.tw/hyreadipadservice3/hyread/v3/asset/ff8081817705f795017769beb6861153/_epub/item/xhtml/p-004.xhtml"

base_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40",
    "Accept": "application/octet-stream",
    "Accept-Encoding": "identity",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "assetUUID": "ff8081817705f795017769beb6861153",
    "Referer": "https://service.ebook.hyread.com.tw/ebookservice/epubreader/hyread/v3/public/b2c7a631bd.w.js",
    "Accept-Ranges": "bytes",
    "Connection": "keep-alive",
    "Content-Length": "71024",
    "Content-Type": "application/octet-stream",
    "Server": "openresty/1.13.6.2",
    "Strict-Transport-Security": "max-age=21600000",
}

download_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40",
    "Referer": base_url,
    "Host": "upos-hz-mirrorakam.akamaized.net",
    "Origin": "https://www.bilibili.com",
    "Accept": "*/*",
    "Accept-Encoding": "identity",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}

# base_response = requests.get(base_url, headers=base_headers)
# print(base_response.cookies)
# html = base_response.text
# print(html)

# book_name = re.search('<h3>(.*?)</h3>', html, re.S).group(1)
# print(book_name)

# video_name = re.search('<span class="tit">(.*?)</span>', html, re.S).group(1) + '.flv'
# print(video_name)
# download_url = re.search('window.__playinfo__={.*?"url":"(.*?)".*?}', html, re.S)
# print(download_url)


"""
test blob download images
"""

url = "https://service.ebook.hyread.com.tw/ebookservice/comic/isThumbJY1wuF3zzUgB9y--l509Zky2ooH8RktyepjZJ2k8WzJVX4X4fus4rt3tzMLYkoIUQrXGxUbvW9V2-7GpCY4b_vMQur78jKeCitcrmg7JA8U/47mK6La04raB6rCP56Cl5Iy36pu_44GE76yY7LiB5bSY4L6_46eR?uuid=8a8a84ca76fb788501773b178a670576"

download_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40",
    "Referer": "https://service.ebook.hyread.com.tw/ebookservice/epubreader/hyread/v3/public/57370eb71f.w.js",
    "assetUUID": "8a8a84ca76fb788501773b178a670576",
    "Host": "upos-hz-mirrorakam.akamaized.net",
    "Origin": "https://www.bilibili.com",
    "Accept": "*/*",
    "Accept-Encoding": "identity",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Headers": "assetuuid,uuid,assetUUID,Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization",
    "Access-Control-Allow-Methods": "GET,OPTIONS",
}

response = requests.get(url, headers=download_headers)
print(response.content)
