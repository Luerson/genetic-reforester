import numpy as np
import matplotlib.pyplot as plt
from .reproduction import reproduction

class reproduction_A(reproduction):

   def reproduction_init(self, lista_solucoes, mapa_binario):
      """
      Realiza cruzamento por interseção lógica entre os dois primeiros indivíduos da lista,
      redistribui os restos dos pais entre os filhos e mostra visualmente.

      Parâmetros:
      - lista_solucoes: lista de arrays numpy booleanos representando soluções válidas
      - mapa_binario: array numpy booleano indicando onde soluções podem existir

      Retorna:
      - offspring1, offspring2: soluções cruzadas e completadas com restos dos pais
      """
      if len(lista_solucoes) < 2:
         raise ValueError("A lista de soluções deve conter pelo menos dois elementos.")

      # Localizações válidas onde podem existir soluções
      pos_validas = np.argwhere(mapa_binario == 1)

      parent1 = np.logical_and(lista_solucoes[0], mapa_binario)
      parent2 = np.logical_and(lista_solucoes[1], mapa_binario)

      # Interseção dos dois pais
      base_offspring = np.logical_and(parent1, parent2)
      offspring1 = base_offspring.copy()
      offspring2 = base_offspring.copy()

      # Restos
      restParent1 = np.logical_xor(parent1, base_offspring)
      restParent2 = np.logical_xor(parent2, base_offspring)

      # --- Função para redistribuir um resto entre dois filhos ---
      def distribuir_restos(resto_mask, filho_a, filho_b, pct_a=0.8):
         indices = np.argwhere(resto_mask)
         np.random.shuffle(indices)
         n_total = len(indices)
         n_a = int(pct_a * n_total)
         for x, y in indices[:n_a]:
            filho_a[x, y] = True
         for x, y in indices[n_a:]:
            filho_b[x, y] = True

      # Distribuindo os restos
      distribuir_restos(restParent1, offspring1, offspring2, pct_a=0.8)
      distribuir_restos(restParent2, offspring2, offspring1, pct_a=0.8)

      # # Visualização dos pais e filhos
      # plt.figure(figsize=(18, 6))

      # plt.subplot(2, 3, 1)
      # plt.imshow(parent1, cmap='coolwarm', vmin=0, vmax=1)
      # plt.title("Parent 1")
      # plt.axis('off')

      # plt.subplot(2, 3, 2)
      # plt.imshow(parent2, cmap='plasma', vmin=0, vmax=1)
      # plt.title("Parent 2")
      # plt.axis('off')

      # plt.subplot(2, 3, 3)
      # plt.imshow(np.logical_and(parent1, parent2), cmap='Greens', vmin=0, vmax=1)
      # plt.title("Interseção (base)")
      # plt.axis('off')

      # plt.subplot(2, 3, 4)
      # plt.imshow(offspring1, cmap='viridis', vmin=0, vmax=1)
      # plt.title("Offspring 1")
      # plt.axis('off')

      # plt.subplot(2, 3, 5)
      # plt.imshow(offspring2, cmap='magma', vmin=0, vmax=1)
      # plt.title("Offspring 2")
      # plt.axis('off')

      # plt.subplot(2, 3, 6)
      # plt.imshow(np.logical_xor(offspring1, offspring2), cmap='hot', vmin=0, vmax=1)
      # plt.title("Diferenças entre filhos")
      # plt.axis('off')

      # plt.tight_layout()
      # plt.show()

      return offspring1, offspring2
