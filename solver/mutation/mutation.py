from abc import ABC, abstractmethod

class mutation(ABC):

    @abstractmethod
    def mut(self, curr_sol):
        pass