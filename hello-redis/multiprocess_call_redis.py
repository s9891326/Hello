import time
import uuid
from multiprocessing import Process, Pool

import redis

r = redis.Redis(host="192.168.223.127", port=6380, password="riu405405")


def acquire_lock(lock_name, p, acquire_timeout=30, lock_timeout=10):
    """
    獲取鎖
    :param lock_name:
    :param p:
    :param acquire_timeout: 每個人能獲得鎖的上限時間
    :param lock_timeout: 鎖的過期時間
    :return:
    """
    identifier = str(uuid.uuid4())
    # 設定當前用戶在特定時間內一定要拿到鎖，若超過acquire_timeout時間都還沒拿到鎖，則return False
    end = time.time() + acquire_timeout
    while time.time() < end:
        # nx: 如果不存在才創建、ex: 過期時間
        # 設置鎖的過期時間，防止deadlock，並返回uuid當作唯一值
        if r.set(lock_name, identifier, ex=lock_timeout, nx=True):
            print(f"進程{p} 獲得鎖")
            return identifier

        time.sleep(0.001)
    return False


def release_lock(lock_name, identifier):
    """
    解鎖
    :param lock_name:
    :param identifier:
    :return:
    """
    # pipe = r.pipeline(True)
    # try:
    #     # 使用 watch 監聽鎖，防止解鎖時，防止解锁时出现删除其他人的锁
    #     pipe.watch(lock_name)
    #     identifier_real = pipe.get(lock_name).decode()
    #
    #     # 驗證鎖的uuid是否相同，相同才能解鎖，否則有可能是別人的鎖
    #     if identifier_real == identifier:
    #         pipe.multi()
    #         pipe.delete(lock_name)
    #         pipe.execute()
    #         return True
    #     pipe.unwatch()
    # except redis.exceptions.WatchError:
    #     pass
    # return False

    unlock_script = """
    if redis.call("get", KEYS[1]) == ARGV[1] then
        return redis.call("del", KEYS[1])
    else
        return 0
    end
    """
    unlock = r.register_script(unlock_script)
    result = unlock(keys=[lock_name], args=[identifier])
    if result:
        return True
    else:
        return False


def exec_test(lock_name, p):
    lock = acquire_lock(lock_name, p)
    if lock:
        print(lock)
        # do something
        # time.sleep(5)
        if release_lock(lock_name, lock):
            print(f"進程{p} 成功解鎖")
        else:
            print(f"進程{p} 解鎖失敗")
    else:
        print(f"進程{p} 拿不到鎖")


if __name__ == '__main__':
    for i in range(10):
        Process(target=exec_test, args=("lock:test", i)).start()


