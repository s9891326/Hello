

# def max_subarray(nums):
    # if not nums:
    #     return 0

    # current_sum = max_sum = nums[0]

    # for num in nums[1:]:
    #     current_sum = max(num, current_sum + num)  # 延續 or 重啟
    #     max_sum = max(max_sum, current_sum)        # 更新最大值

    # return max_sum

# def max_profit(prices):
    # a =  [[1, 2], [3, 4]]
    # if not prices:
    #     return 0

    # min_price = prices[0]
    # max_profit = 0

    # a = {len: 1}

    # for price in prices:
    #     min_price = min(min_price, price)          # 找到最低點
    #     max_profit = max(max_profit, price - min_price)  # 計算獲利

    # return max_profit


# ```
# SELECT 
#     ROUND(
#         100.0 * AVG(CASE WHEN deliver_date = order_date THEN 1 ELSE 0 END),
#         2
#     ) AS real_time_order_percentage
# FROM orders;

# DELETE FROM orders
# WHERE id NOT IN (
#     SELECT MIN(id)
#     FROM orders
#     GROUP BY email
# );
# ```


# if __name__ == "__main__":
#     # print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
#     # print(max_subarray([10,-5,7,6,-1,-3]))    # Output: 18

#     # print(max_profit([7,1,5,3,6,4]))  # Output: 5
#     a=[1, 2, 3, 4, 5]
#     # del a[2]
#     # a.remove(3)
#     a[2:2] = []
#     print(a)  # Output: [1, 2, 4, 5]



### 連習asyncio await
# import asyncio

# async def fetch_data(url: str) -> str:
#     print(f"Start fetching {url} data...")
#     await asyncio.sleep(2)  # 模擬 I/O 操作
#     print(f"Data fetched {url}")
#     return f"Data from {url}"


# """
# 這證明了兩個 fetch_data 協程並沒有一個接一個地執行，而是在等待 asyncio.sleep(2) 時，
# 將控制權交給了另一個協程，讓它們可以同時運行。
# 這就是 asyncio 在處理 I/O 密集型任務時，能夠顯著提高效率的原因。
# """
# async def main():
#     print("Main start")

#     task1 = fetch_data("'https://api.example.com/data1')")
#     task2 = fetch_data("'https://api.example.com/data2')")

#     # 使用 await asyncio.gather 來同時運行這些任務
#     # 它會等待所有任務完成，並返回一個包含所有結果的列表
#     results = await asyncio.gather(task1, task2)

#     print('所有任務都已完成')
#     for result in results:
#         print(result)

#     print('應用程式結束')


# if __name__ == "__main__":
#     asyncio.run(main())


"""
Python 3.9 - 字典合併與更新
Python 3.10 - 模式匹配 (Structural Pattern Matching)
Python 3.11 - 效能與錯誤回溯優化
"""

# def get_info(person: dict) -> str:
#     match person:
#         case {"name": name, "age": age} if age >= 18:
#             return f"{name} is an adult."
#         case {"name": name, "age": age}:
#             return f"{name} is a minor."
#         case {"name": name, "city": city}:
#             return f"{name} lives in {city}."
#         case _:
#             return "Unknown person"

# def get_status_code(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown Status"

# if __name__ == "__main__":
#     dict1 = {"a": 1, "b": 2}
#     dict2 = {"b": 3, "c": 4}
#     print(dict1 | dict2)  # Output: {'a': 1, 'b': 3, 'c': 4}
#     print(dict1 | {"d": 5})  # Output: {'a': 1, 'b': 2, 'd': 5}

#     print(get_info({"name": "Eddy", "age": 18}))
#     print(get_info({"name": "Eddy", "city": "Taipei"}))
    
#     print(get_status_code(200))
#     print(get_status_code(404))


"""
python class naming conventions
"""
class Animal:
    def __init__(self):
        self._name = "name"
        self.__age = 20
        self._type_ = "type"
        self.__weight__ = 30


if __name__ == "__main__":
    animal = Animal()
    print(animal._name)          # 單下劃線，表示受保護的屬性
    # print(animal.__age)          # 雙下劃線，會導致名稱改寫，無法直接訪問
    print(animal._Animal__age)   # 可以通過這種方式訪問雙下劃線屬性
    print(animal._type_)         # 單下劃線結尾，表示受保護的屬性
    print(animal.__weight__)     # 雙下劃線結尾，不會導致名稱改寫，可以直接訪問

