from factory import factory
import matplotlib.pyplot as plt
import numpy as np
import random

my_data         = factory.get_data_A()
my_mutation     = factory.get_mutation_A()
my_selector     = factory.get_selector_B()
my_constructive = factory.get_constructive_A()
my_reproduction = factory.get_reproduction_A()
my_generation   = factory.get_generation_A()

my_solver       = factory.get_solver_A()

my_solver.set_data(my_data)
my_solver.set_selector(my_selector)
my_solver.set_mutation(my_mutation)
my_solver.set_constructive(my_constructive)
my_solver.set_reproduction(my_reproduction)
my_solver.set_generation(my_generation)

# caminho_entrada = input("caminho do arquivo de entrada:")
caminho_entrada = "input/uso_solo_2019.tif"
# caminho_saida   = input("caminho do arquivo de saida:")

my_data.read_Data(caminho_entrada)

my_data.show_data()

solucoes = my_constructive.construct_init(my_data.mapa_binario_restauravel)

#visualizar(solucoes)
# comparar_solucoes(solucoes[0], solucoes[1])

print(f"Total de soluções antes da seleção: {len(solucoes)}")
solucoes_selecionadas = my_selector.select(solucoes, my_data.mapa_binario_floresta)
print(f"Total de soluções após seleção: {len(solucoes_selecionadas)}")

# comparar_solucoes(solucoes[0], solucoes_selecionadas[0])


my_reproduction.reproduction_init(solucoes, my_data.mapa_binario_restauravel)

print(my_solver.solve())

def visualizar(solucoes):
    plt.figure(figsize=(15, 8))
    
    for i, sol in enumerate(solucoes, 1):
        plt.subplot(3, 4, i)

        # Mostra só os pixels ativados em cada solução
        plt.imshow(sol, cmap='jet', vmin=0, vmax=1)
        plt.title(f"Solução {i}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()

def comparar_solucoes(sol1, sol2):
    plt.figure(figsize=(15, 4))

    # Solução 1 com colormap 
    plt.subplot(1, 3, 1)
    plt.imshow(sol1, cmap='coolwarm', vmin=0, vmax=1)
    plt.title("Solução 1")
    plt.axis('off')

    # Solução 2 com colormap 
    plt.subplot(1, 3, 2)
    plt.imshow(sol2, cmap='plasma', vmin=0, vmax=1)
    plt.title("Solução 2")
    plt.axis('off')

    # Diferença (onde sol1 ≠ sol2) 
    diff = np.logical_xor(sol1, sol2).astype(int)
    plt.subplot(1, 3, 3)
    plt.imshow(diff, cmap='hot', vmin=0, vmax=1)
    plt.title("Diferença (XOR)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

visualizar(solucoes)
