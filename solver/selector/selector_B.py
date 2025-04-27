import random
from .selector import selector
import numpy as np
import copy
import pylandstats as pls
import matplotlib.pyplot as plt

class selector_B(selector):
    def select(self, solucoes, mapa_floresta):
        # Passo 1: Igual a selector_A
        solucoes_combinadas = []
        for sol in solucoes:
            combinada = np.logical_or(sol, mapa_floresta).astype(int)
            solucoes_combinadas.append(combinada)
        
        # Passo 2: igual a selector_A, mas com métrica diferente
        scores = []
        for i, combinada in enumerate(solucoes_combinadas):
            new_combinada = combinada + 1  
            paisagem = pls.Landscape(new_combinada, res=(30, 30))
            try:
                contagion = paisagem.contagion()
                lsi = paisagem.landscape_shape_index()
                score = contagion / lsi
            except:
                score = 0  
            scores.append(score)

        # Passo 3: Normalizar scores para probabilidades (0% a 100%)
        scores = np.array(scores)
        scores_normalizados = (scores / scores.sum()) * 100  

        # Passo 4: Seleção probabilística 
        sobreviventes = []
        indices = list(range(len(solucoes)))  
        n_selecionar = len(solucoes) // 2    
        for _ in range(n_selecionar):
            # Escolha aleatória baseada nas probabilidades
            escolhido = random.choices(indices, weights=scores_normalizados, k=1)[0]
            sobreviventes.append(solucoes[escolhido])
            
            # Remove o escolhido e renormaliza as probabilidades
            indices.remove(escolhido)
            scores_normalizados = np.delete(scores_normalizados, escolhido)
            scores_normalizados = (scores_normalizados / scores_normalizados.sum()) * 100

        return sobreviventes