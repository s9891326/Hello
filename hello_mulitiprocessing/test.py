from multiprocessing import Process, Pool
import os, time


def main_map(i):
    result = i * i
    return result

if __name__ == '__main__':
    inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 設定處理程序數量
    pool = Pool(4)

    # 運行多處理程序
    pool_outputs = pool.map(main_map, inputs)

    # 輸出執行結果
    print(pool_outputs)
