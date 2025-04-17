from abc import ABC, abstractmethod

class solver(ABC):

    @abstractmethod
    def solve(self):
        pass