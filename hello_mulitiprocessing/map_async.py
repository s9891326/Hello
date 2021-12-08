from multiprocessing import Process, Pool
import os, time
import logging


logging.basicConfig(filename="map_async.log", level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

def main_map(i):
    result = i * i
    # print(f"子處理程序 ID: {os.getpid()}, 運送結果: {result}")
    logging.debug(f"子處理程序 ID: {os.getpid()}, 運送結果: {result}")
    return result


def show(get_result):
    print('Callback: {} PID: {}'.format(get_result, os.getpid()))


if __name__ == '__main__':

    print('主處理程序 ID:', os.getpid())
    pool = Pool(4)

    results = pool.map_async(main_map, [3, 5, 7, 9, 11, 13, 15], callback=show)
    pool.close()
    pool.join()