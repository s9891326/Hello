import asyncio
import time

now = lambda: time.time()

async def dosomething(num):
    print('第 {} 任務，第一步'.format(num))
    await asyncio.sleep(1)
    print('第 {} 任務，第二步'.format(num))


def hello():
    start = now()
    tasks = [dosomething(i) for i in range(5)]
    asyncio.run(asyncio.wait(tasks))
    print('TIME: ', now() - start)


def set_event_loop_policy() -> None: ...


async def async_func():
    return 1

async def await_func():
    result = await async_func()
    print(result)


if __name__ == "__main__":
    hello()

    # asyncio.run(await_func())
    # s = now()
    # for i in range(5):
    #     dosomething2(i)
    # print(f"time: {now() - s}")
