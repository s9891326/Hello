import asyncio
import time

# 一開始 同步的效果: 等到一個結束再跑另外一個
def first():
    async def visit_url(url, response_time):
        """訪問 url"""
        await asyncio.sleep(response_time)
        return f"訪問{url}, 已得到返回結果"

    start_time = time.perf_counter()
    task = visit_url('http://wangzhen.com', 2)
    asyncio.run(task)
    
    task2 = visit_url('http://another.com', 3)
    asyncio.run(task2)
    print(f"消耗時間：{time.perf_counter() - start_time}")


# 使用非同步的: 不等第一個跑完 直接跑第二個
def second():
    async def visit_url(url, response_time):
        """訪問 url"""
        await asyncio.sleep(response_time)
        return f"訪問{url}, 已得到返回結果"

    async def run_task():
        """收集子任務"""
        task = visit_url('http://wangzhen.com', 2)
        task_2 = visit_url('http://another', 3)
        task1 = asyncio.create_task(task)
        task2 = asyncio.create_task(task_2)

        await task1
        await task2
    
    start_time = time.perf_counter()
    asyncio.run(run_task())
    print(f"消耗時間：{time.perf_counter() - start_time}")


if __name__ == '__main__':
    # first()
    second()
