import asyncio
import random

queue = asyncio.Queue()

async def producer(name, count):
    for i in range(count):
        await asyncio.sleep(random.uniform(0.1, 0.3))
        item = f"{name}-item-{i}"
        await queue.put(item)
        print(f"Producer {name} produced {item}")
    print(f"Producer {name} finished.")

async def consumer(name):
    while True:
        item = await queue.get()
        print(f"Consumer {name} consumed {item}")
        await asyncio.sleep(random.uniform(0.2, 0.6))
        queue.task_done()

async def main():
    producers = [asyncio.create_task(producer(f"P{i}", 5)) for i in range(2)]
    consumers = [asyncio.create_task(consumer(f"C{i}")) for i in range(3)]

    outer = await asyncio.gather(*producers)
    print(f"gather output {outer}")
    await queue.join()  # 等所有任務都被消費完

    for c in consumers:
        c.cancel()  # 停止消費者
    outer = await asyncio.gather(*consumers, return_exceptions=True)
    print(outer)
    print("All done.")

if __name__ == "__main__":
    asyncio.run(main())


"""
asyncio.create_task() 用於建立並啟用一個task（協程任務）。
asyncio.gather() (可以接收coroutine or task) 可以同時等待多個協程任務完成，並收集它們的結果。

create_task 用來「啟動」任務，gather 用來「收集」任務。
"""


# async def worker(name, delay):
#     await asyncio.sleep(delay)
#     return f"{name} done"

# async def main():
#     # 建立並啟動任務
#     t1 = asyncio.create_task(worker("A", 2))
#     t2 = asyncio.create_task(worker("B", 1))

#     print("Tasks created, doing something else...")
#     # 收集結果
#     # result = await t1
#     # result2 = await t2
#     # print(result, result2)
#     result = await asyncio.gather(t1, t2)
#     print(result)

# asyncio.run(main())
