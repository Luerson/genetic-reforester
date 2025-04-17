from .data import data 

class data_A(data):

    def __init__(self):
        self.mapa_binario = None
    
    def read_Data(self, path: str):
        return "lendo: " + str(path)

    def write_Data(self, path: str):
        return "escrevendo: " + str(path)