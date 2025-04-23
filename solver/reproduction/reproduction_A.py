import numpy as np
from .reproduction import reproduction

class reproduction_A(reproduction):

   def reproduction_init(self, lista_solucoes, mapa_binario):
      """
      Realiza cruzamento genético entre pares aleatórios de soluções booleanas
      respeitando um mapa binário de posições válidas.

      Parâmetros:
      - lista_solucoes: lista de arrays numpy booleanos (soluções atuais)
      - mapa_binario: array booleano indicando posições válidas (1 = pode ser ocupado)

      Retorna:
      - lista com os indivíduos originais + filhos gerados (tamanho final: 2x original)
      """

      n = len(lista_solucoes)
      indices = np.random.permutation(n)  # Embaralha os índices para formar pares aleatórios
      nova_lista = lista_solucoes.copy()  # Cria uma nova lista para armazenar pais + filhos

      def distribuir_restos(resto_mask, filho_a, filho_b, pct_a=0.8):
         """
         Distribui os pixels ativos do resto de um pai entre dois filhos.
         - pct_a: porcentagem do resto que vai para o primeiro filho.
         """
         indices = np.argwhere(resto_mask)  # Posições do resto
         np.random.shuffle(indices)  # Embaralha as posições
         n_total = len(indices)
         n_a = int(pct_a * n_total)  # Quantidade que vai para filho_a
         for x, y in indices[:n_a]:
            filho_a[x, y] = True
         for x, y in indices[n_a:]:
            filho_b[x, y] = True

      # Itera sobre pares de soluções para cruzamento
      for i in range(0, n, 2):
         idx1, idx2 = indices[i], indices[i + 1]
         parent1 = np.logical_and(lista_solucoes[idx1], mapa_binario)  # Garante que só usa áreas válidas
         parent2 = np.logical_and(lista_solucoes[idx2], mapa_binario)

         # Interseção: base comum dos dois pais
         base_offspring = np.logical_and(parent1, parent2)
         offspring1 = base_offspring.copy()
         offspring2 = base_offspring.copy()

         # Calcula os "restos" dos pais (valores que estão em apenas um dos pais)
         restParent1 = np.logical_xor(parent1, base_offspring)
         restParent2 = np.logical_xor(parent2, base_offspring)

         # Distribui os restos entre os filhos
         distribuir_restos(restParent1, offspring1, offspring2, pct_a=0.8)
         distribuir_restos(restParent2, offspring2, offspring1, pct_a=0.8)

         # Adiciona os filhos à nova lista de soluções
         nova_lista.append(offspring1)
         nova_lista.append(offspring2)

      return nova_lista