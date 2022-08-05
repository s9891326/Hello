# 外觀模式： 簡化複雜物件的存取問題
# 外觀模式用來簡化複雜系統的訪問。
# 通過簡化的介面只訪問需要的部分，隱藏系統複雜性。
# 想像一下公司接線員，雖然公司內部運行機制比較複雜，但是接線員可以迅速幫你解決特定問題。 我們以實現個簡單的作業系統範例說明外觀模式：


# 這種設計模式的精神，在於將多個複雜的處理流程，包裝成一個接口進行執行
#
# 就像客服系統一樣，統一由客服將問題轉介到各個處理流程上

from abc import ABCMeta, abstractmethod
from enum import Enum

class State(Enum):
    new = 1
    running = 2
    sleeping = 3
    restart = 4
    zombie = 5


class Server(metaclass=ABCMeta):
    """ 抽象基类 """
    
    @abstractmethod
    def __init__(self):
        self.name = ""

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def boot(self):
        pass
    
    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self):
        """actions required for initializing the file server"""
        super().__init__()
        self.name = "FileServer"
        self.state = State.new
    
    def boot(self):
        """actions required for booting the file server"""
        print("booting the {}".format(self))
        self.state = State.running
    
    def kill(self, restart=True):
        """actions required for killing the file server"""
        print("Killing {}".format(self))
        self.state = State.restart if restart else State.zombie
    
    def create_file(self, user, name, permissions):
        """check validity of permissions, user rights, etc."""
        print("trying to create the file '{}' for user '{}' with permissions {}".format(name, user, permissions))


class ProcessServer(Server):
    def __init__(self):
        """actions required for initializing the process server"""
        super().__init__()
        self.name = "ProcessServer"
        self.state = State.new
    
    def boot(self):
        """actions required for booting the process server"""
        print("booting the {}".format(self))
        self.state = State.running
    
    def kill(self, restart=True):
        """actions required for killing the process server"""
        print("Killing {}".format(self))
        self.state = State.restart if restart else State.zombie
    
    def create_process(self, user, name):
        """check user rights, generate PID, etc."""
        print("trying to create the process '{}' for user '{}'".format(name, user))


class OperatingSystem:
    """
    实现外观模式，外部使用的代码不必知道 FileServer 和 ProcessServer的
    内部机制，只需要通过 OperatingSystem类调用
    """
    
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()
    
    def start(self):
        """ 被客户端代码使用 """
        [i.boot() for i in (self.fs, self.ps)]
    
    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)
    
    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')


if __name__ == '__main__':
    # print(State.new)
    main()
