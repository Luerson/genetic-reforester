from .selector import selector
import numpy as np
import copy
import pylandstats as pls
import matplotlib.pyplot as plt

class selector_A(selector):

    def select(self, solucoes, mapa_floresta):
        # Passo 1: Combinar cada solução com o mapa de floresta
        solucoes_combinadas = []
        for sol in solucoes:
            # Criar cópia para não modificar a solução original
            combinada = copy.deepcopy(sol)

            combinada
            # Combinar com o mapa de floresta (OR lógico), 1=floresta/reflorestamento
            combinada = np.logical_or(combinada, mapa_floresta).astype(int)

            solucoes_combinadas.append(combinada)
        
        # Passo 2: Calcular métricas para cada solução combinada
        scores = []
        for i, combinada in enumerate(solucoes_combinadas):  # Corrigido: usar enumerate
            # Criar objeto Landscape do pylandstats, resolução 1x1 pois são pixels binários
            new_combinada = combinada + 1
            paisagem = pls.Landscape(new_combinada, res=(30, 30))
            
            # Calcular métricas importantes para conectividade
            try:
                contagion = paisagem.contagion()
                lsi = paisagem.landscape_shape_index()
            except:
                lsi = 0
                contagion = 0
                
            scores.append(contagion/lsi)
            # print(f"Solução {i}: lsi = {lsi}")
            # print(f"Solução {i}: contagion = {contagion}")

            # # Visualizar a solução e a solução combinada 
            # plt.figure(figsize=(15, 4))
            # plt.subplot(1, 2, 1)
            # plt.imshow(solucoes[i], cmap='coolwarm', vmin=0, vmax=1)  # Mapa de cores mais adequado
            # plt.title(f"Solução {i}")
            # plt.axis('off')

            # plt.subplot(1, 2, 2)
            # plt.imshow(combinada, cmap='Greens', vmin=0, vmax=1)
            # plt.title(f"Solução {i} + Mapa de Floresta")
            # plt.axis('off')

            # plt.tight_layout()
            # plt.show()
        
        # Passo 3: Ordenar soluções pelos scores (melhores primeiro)
        indices_ordenados = np.argsort(scores)[::-1]  
        
        # Passo 4: Selecionar as N/2 melhores soluções
        n_selecionar = len(solucoes) // 2
        melhores_indices = indices_ordenados[:n_selecionar]
        melhores_solucoes = [solucoes[i] for i in melhores_indices]

        melhores_valores = [scores[i] for i in melhores_indices]
        print(max(melhores_valores))
        
        return melhores_solucoes