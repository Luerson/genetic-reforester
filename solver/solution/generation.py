from abc import ABC, abstractmethod

class generation(ABC):

    @abstractmethod
    def add_member(self, member):
        pass
    
    @abstractmethod
    def del_member(self, member):
        pass