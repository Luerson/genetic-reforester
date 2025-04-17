from abc import ABC, abstractmethod

class selector(ABC):

    @abstractmethod
    def select(self, population, forest):
        pass