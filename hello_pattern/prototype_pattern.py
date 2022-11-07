# 原型模式：解決對象拷貝問題
# 這是創建模式中的最後一個，用來克隆一個對象，有點像生物學中的有絲分裂。
# 我們可以使用python內置的copy模組實現。
# 拷貝分為深拷貝和淺拷貝，深拷貝會遞歸複製並創建新物件，而淺拷貝會利用引用指向同一個物件.
# 深拷貝的優點是對象之間互不影響，但是會耗費資源，創建比較耗時; 如果不會修改物件可以使用淺拷貝，更加節省資源和創建時間。
# “淺副本構造一個新的復合物件，然後（在可能的範圍內）插入對原始物件的引用。
# 深度副本構造一個新的復合物件，然後以遞歸方式將原始物件的副本插入其中。

# 這種設計模式的用途在於，有很多人想針對同一個範本（物件）進行修改時，可以採用這種設計模式
#
# 使用方法是把原本的物件抄寫一份，讓超寫出來的物件不會影響到原本的物件
#
# 主要的實現方式是透過python copy package裡面的deepcopy來實現

import copy
from collections import OrderedDict



class Book:
    def __init__(self, name, authors, price, **rest):
        """
        Examples of rest: publisher, length, tags, publication date
        """
        self.name = name
        self.authors = authors
        self.price = price  # in US dollars
        self.__dict__.update(rest)
    
    def __str__(self):
        result = []
        for k, v in self.__dict__.items():
            result.append(f"{k}: {v}")
            if k == "price":
                result.append("$")
            result.append("\n")
        return "".join(result)
        
        # mylist = []
        # ordered = OrderedDict(sorted(self.__dict__.items()))
        # for i in ordered.keys():
        #     mylist.append('{}: {}'.format(i, ordered[i]))
        #     if i == 'price':
        #         mylist.append('$')
        #     mylist.append('\n')
        # return ''.join(mylist)


class Prototype:
    def __init__(self):
        self.objects = {}
    
    def register(self, identifier, obj):
        self.objects[identifier] = obj
    
    def unregister(self, identifier):
        del self.objects[identifier]
    
    def clone(self, identifier, **attr):
        """ 实现对象拷贝 """
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)  # 实现拷贝时自定义更新
        return obj


def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'),
              price=118, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structures'))
    
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language (ANSI)', price=48.99, length=274,
                         publication_date='1988-04-01', edition=2)
    
    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))
    for i in (b1, b2):
        print(i)


if __name__ == '__main__':
    main()
