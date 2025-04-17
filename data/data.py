from abc import ABC, abstractmethod

class data(ABC):
    
    @abstractmethod
    def read_Data(self, path: str):
        pass

    @abstractmethod
    def write_Data(self, path: str):
        pass