from .constructive import constructive
import numpy as np

class constructive_A(constructive):
    def construct_init(self, mapa_binario):
        # Passo 1: Identificar pixels válidos
        pos_validas = np.argwhere(mapa_binario == 1)
        n_validos = len(pos_validas)
        n_preencher = int(0.3 * n_validos)
        
        solucoes = []
    
        # Passo 2: Gerar 12 soluções com conjuntos diferentes de pixels
        for k in range(192):
            solucao = np.zeros_like(mapa_binario)
            
            # Seleciona 20% dos pixels válidos ALEATORIAMENTE (sem repetição dentro da mesma solução)
            indices = np.random.choice(n_validos, size=n_preencher, replace=False)
            
            # Ativa os pixels selecionados
            for idx in indices:
                i, j = pos_validas[idx]
                solucao[i, j] = 1
            
            solucoes.append(solucao)
            

        return solucoes
