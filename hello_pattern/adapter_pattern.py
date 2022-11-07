# 適配器模式： 解決介面不相容問題
# 開始介紹結構型設計模式，結構型設計模式通過組合對象來實現新功能。
# 適配器模式通過引入間接層來實現不相容介面之間的適配。
# 現實中最好的例子就是手機充電口，不同型號安卓手機都可以用同樣的充電線充電。
# 在python中可以通過繼承實現適配，也可以通過使用class的__dict__屬性。
# 開閉原則：適配器模式和OOP中的開閉原則關係密切，開閉原則強調對擴展開放，對修改關閉。
# 通過適配器模式我們可以通過創建適配器模式在不修改原有類代碼的情況下實現新的功能。


# Adapter 的設計精神在於將調用的接口一致化，或是同一個功能與系統要交互配置時，可以不改動原本的代碼，採用一樣的方式調用各種功能
#
# 通常會出現在兩個接口不一樣的功能時，要統一調用的方法
#
# 尤其是要使用外部系統的功能時，可以採用這種模式

class Computer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} computer'.format(self.name)
    
    def execute(self):
        """ call by client code """
        return 'execute a program'


class Synthesizer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)
    
    def play(self):
        return 'is playing an electroinc song'


class Human:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} human'.format(self.name)
    
    def speak(self):
        return 'says hello'


class Adapter:
    def __init__(self, obj, adapted_methods):
        """ 不使用继承，使用__dict__属性实现适配器模式 """
        self.obj = obj
        self.__dict__.update(adapted_methods)
    
    def __str__(self):
        return str(self.obj)


# 适配器使用示例
def main():
    objs = [Computer('Asus')]
    synth = Synthesizer('moog')
    objs.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Wnn')
    objs.append(Adapter(human, dict(execute=human.speak)))
    
    for o in objs:
        # 用统一的execute适配不同对象的方法，这样在无需修改源对象的情况下就实现了不同对象方法的适配
        print('{} {}'.format(str(o), o.execute()))


if __name__ == "__main__":
    main()
