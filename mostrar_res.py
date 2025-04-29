import matplotlib.pyplot as plt

def ler_valores_float(caminho_arquivo):
    valores = []
    
    with open(caminho_arquivo, 'r') as f:
        for linha in f:
            linha = linha.strip()
            try:
                valor = float(linha)
                if valor > 10:
                    continue
                valores.append(valor)
            except ValueError:
                continue
    
    return valores

def plotar_duas_variaveis(valores1, valores2, label1='Variável 1', label2='Variável 2'):
    plt.figure(figsize=(10, 6))
    
    plt.plot(range(len(valores1)), valores1, marker='o', label=label1)
    plt.plot(range(len(valores2)), valores2, marker='s', label=label2)
    
    plt.title('Evolução a cada geração')
    plt.xlabel('Geração')
    plt.ylabel('(contagion)/(lsi)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Exemplo de uso:
caminho1 = 'Litoral_A.txt'
caminho2 = 'Litoral_B.txt'

valores1 = ler_valores_float(caminho1)
valores2 = ler_valores_float(caminho2)

plotar_duas_variaveis(valores1, valores2, label1='selector hierárquico', label2='selector roleta')
