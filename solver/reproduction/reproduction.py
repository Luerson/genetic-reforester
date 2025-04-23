from abc import ABC, abstractmethod

class reproduction(ABC):

    @abstractmethod
    def reproduction_init(self, lista_solucoes, mapa_binario):
        pass