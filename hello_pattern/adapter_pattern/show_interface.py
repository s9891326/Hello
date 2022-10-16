from abc import ABC, abstractmethod


class ShowInterface(ABC):
    @abstractmethod
    def show(self):
        pass
