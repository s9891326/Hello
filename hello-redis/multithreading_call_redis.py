import time
from multiprocessing import Process
from threading import Thread

import redis

total_votes = 20


def get_ticket(r, i, key):
    global total_votes

    print(f"線程{i} get ticket")
    # with r.lock(key):
    #     print(f"線程{i} get key: {r.get(key)}")
    #
    #     if total_votes < 1:
    #         print(f"線程{i} 沒票了GG")
    #         return
    #
    #     total_votes -= 1
    #     print(f"線程{i} get ticket, 剩餘{total_votes}")

    lock = r.lock(key)
    try:
        if lock.acquire(blocking=True, blocking_timeout=3):
            print(f"線程{i} get key: {r.get(key)}")
            # time.sleep(4)

            if total_votes < 1:
                print(f"線程{i} 沒票了GG")
                return

            total_votes -= 1
            print(f"線程{i} get ticket, 剩餘{total_votes}")
    except:
        pass
    finally:
        lock.release()


if __name__ == '__main__':
    pool = redis.ConnectionPool(
        host="192.168.223.127",
        port=6380, db=0,
        password="riu405405",
        socket_connect_timeout=3,
        decode_responses=True
    )
    r = redis.Redis(connection_pool=pool)

    st = time.time()

    for i in range(30):
        t = Thread(target=get_ticket, args=(r, i, 'my_lock'))
        t.start()

    print(f"finish time: {time.time() - st}")

    # for i in range(0, 9):
    #     Process(target=get_ticket, args=(r, i, 'test')).start()
