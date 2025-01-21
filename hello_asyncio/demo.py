import collections
import time
from typing import List


class EventLoop:
    def __init__(self):
        self.ready = collections.deque()
        self.scheduled: List["Handle"] = []

    def run(self, coro):
        self.ready.append(Task(coro))

        while 1:
            for handle in self.scheduled:
                if time.time() >= handle.end_time:
                    self.scheduled.remove(handle)
                    self.ready.append(handle)

            if self.ready:
                task = self.ready.popleft()
                task()


loop = EventLoop()


class Task:
    def __init__(self, coro):
        self.coro = coro

    def __call__(self, *args, **kwargs):
        try:
            result = next(self.coro)
        except StopIteration:
            pass
        else:
            if isinstance(result, Future):
                result.add_done_callback(self.__call__)


class Future:
    def __init__(self):
        self.cb = []

    def add_done_callback(self, cb):
        self.cb.append(cb)

    def run_main_loop(self):
        for cb in self.cb:
            cb()


class Handle:
    def __init__(self, cb, end_time):
        self.cb = cb
        self.end_time = end_time

    def __call__(self, *args, **kwargs):
        self.cb()


def sleep(second):
    print(f"sleep {second}")
    future = Future()
    end_time = time.time() + second

    loop.scheduled.append(Handle(lambda: future.run_main_loop(), end_time))

    yield future


def main():
    print("hi")
    yield from sleep(1)
    print("hi2")
    yield from sleep(2)
    print("hi3")
    yield from sleep(3)
    print("end")


if __name__ == "__main__":
    loop.run(main())
