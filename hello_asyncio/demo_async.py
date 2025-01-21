import collections
import time


class EventLoop:
    def __init__(self):
        self.scheduled = []
        self.ready = collections.deque()

    def run(self, coro):
        self.ready.append(Task(coro))

        while True:
            for schedule in self.scheduled:
                if time.time() >= schedule.end_time:
                    self.scheduled.remove(schedule)
                    self.ready.append(schedule)

            while len(self.ready) != 0:
                handle = self.ready.popleft()
                handle()


class Task:
    def __init__(self, coro):
        self.coro = coro

    def __call__(self):
        try:
            result = next(self.coro)
        except StopIteration:
            pass
        else:
            if isinstance(result, Future):
                result.add_done_callback(self.__call__)


class Handle:
    def __init__(self, callback, end_time):
        self.callback = callback
        self.end_time = end_time

    def __call__(self):
        self.callback()


loop = EventLoop()


class Future:
    def __init__(self):
        self.callbacks = []
        self.result = None

    def set_result(self, result):
        self.result = result
        for callback in self.callbacks:
            callback()

    def add_done_callback(self, callback):
        self.callbacks.append(callback)

    def __iter__(self):
        if self.result is None:
            # 第一次 await Future 時 -- 如果還沒完成，先將 future 自己 yield 出去，
            # Task 那邊收到 yield 的 result 若是 Future 會去偵聽 future 的完成事件 (via add_done_callback)，
            # 確認 future 完成後才會再呼叫一次這個 coro 繼續往下執行
            yield self
        # 呈上，預期收到 future 完成事件後才會執行到這邊，所以如果此時還判斷出 not done() 就代表有鬼
        if self.result is None:
            raise RuntimeError("await wasn't used with future")
        return self.result


def sleep(seconds: int):
    future = Future()
    end_time = time.time() + seconds
    schedule = Handle(lambda: future.set_result("DONE!"), end_time)
    loop.scheduled.append(schedule)
    yield future


def main():
    print("Sleeping...")
    yield from sleep(1)
    print("Hi...")
    yield from sleep(3)
    print("Yo...")
    yield from sleep(6)
    print("End!")


if __name__ == '__main__':
    loop.run(main())
