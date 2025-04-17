from abc import ABC, abstractmethod

class reproduction(ABC):

    @abstractmethod
    def rep(self, curr_sol_1, curr_sol_2):
        pass