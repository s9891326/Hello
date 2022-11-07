from abc import ABC, abstractmethod


class BasicVideo(ABC):
    def make(self):
        return self.generate_ideas() + \
               "、" + self.shoot() + \
               "、" + self.editing() + \
               "、" + self.upload()
    
    def shoot(self):
        return "拍攝"
    
    def upload(self):
        return "上傳影片"
    
    @abstractmethod
    def editing(self):
        pass
    
    @abstractmethod
    def generate_ideas(self):
        pass
