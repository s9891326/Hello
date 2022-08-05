# 裝飾器模式： 無需子類化實現擴展物件功能問題
# 通常給一個物件添加新功能有三種方式：
# - 直接給對象所屬的類添加方法。
# - 使用『組合』
# - 使用『繼承』，優先使用組合而非繼承。
# 裝飾器模式提供了第四種選擇，通過動態改變物件擴展物件功能。
# 其他程式設計語言通常使用繼承實現裝飾器裝飾器模式，而python內置了裝飾器。
# 裝飾器有很多用途，比如數據校驗，事務處理，緩存，日誌等。
# 比如用裝飾器實現一個簡單的緩存，python3.5自帶了functools.lru_cache


# 裝飾器的功能在於擴充現有物件或Function的功能
#
# 在Python中建置好的新功能，可以透過＠對現有物件進行擴充
#
# 常見的擴充範疇為：資料驗證、Caching、Logging、Monitoring、Debugging、Business Rules、Excryption、Compression…

from functools import wraps


def memoize(fn):
    known = dict()
    
    @wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    
    return memoizer


@memoize
def fibonacci(n):
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(10))
