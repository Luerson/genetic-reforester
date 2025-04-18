import rasterio
import numpy as np
from .data import data
import matplotlib.pyplot as plt

class data_A(data):
    def __init__(self):
        self.mapa_binario_floresta     = None
        self.mapa_binario_restauravel  = None
        self.mapa_MAPBIOMAS            = None
        self.meta                      = None

    def read_Data(self, path: str):
        with rasterio.open(path) as src:
            # Lê a única banda que contém as classificações
            mapa = src.read(1).astype(np.int32)
            self.mapa_MAPBIOMAS = mapa
            self.meta = src.meta.copy()

            # Floresta = classes 3, 4, 5, 6, 49
            classes_floresta = [3, 4, 5, 6, 49]
            self.mapa_binario_floresta = np.isin(mapa, classes_floresta).astype(np.uint8)
            
            # Restaurável = pastagem (15) ou mosaico de uso (21)
            classes_restauraveis = [15, 21]
            self.mapa_binario_restauravel = np.isin(mapa, classes_restauraveis).astype(np.uint8)

        return f"Arquivo lido com sucesso: {path}"
    
    def show_data(self):
        if self.mapa_MAPBIOMAS is None:
            print("❌ Nenhum dado carregado. Use read_Data(path) antes.")
            return

        fig, axs = plt.subplots(1, 3, figsize=(18, 5))
        
        # 1. Mapa completo do MapBiomas
        axs[0].imshow(self.mapa_MAPBIOMAS, cmap='tab20')
        axs[0].set_title("Mapa MapBiomas")
        axs[0].axis('off')
        
        # 2. Máscara Floresta
        axs[1].imshow(self.mapa_binario_floresta, cmap='Greens', vmin=0, vmax=1)
        axs[1].set_title("Máscara Floresta (3, 4, 5, 6, 49)")
        axs[1].axis('off')

        # 3. Máscara Restaurável
        axs[2].imshow(self.mapa_binario_restauravel, cmap='OrRd', vmin=0, vmax=1)
        axs[2].set_title("Máscara Restaurável (15, 21)")
        axs[2].axis('off')

        plt.tight_layout()
        plt.show()
