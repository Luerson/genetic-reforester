import rasterio
import numpy as np
import matplotlib.pyplot as plt

# === 1. Caminho para o novo raster do MapBiomas ===
entrada_raster = "uso_solo_2019.tif"  # Nome do arquivo exportado do GEE
saida_mascara = "mascara_restauravel_2019.tif"

# === 2. Abrir o raster de uso do solo ===
with rasterio.open(entrada_raster) as src:
    uso_solo = src.read(1)
    perfil = src.profile

# === 3. Criar máscara de áreas restauráveis ===
# Exemplo: pastagem (classe 15), mosaico de agricultura/pastagem (classe 21) — opcional
classes_restauraveis = [15, 21]  # ou [15, 21] se quiser incluir mosaico

# Como o GEE exporta diretamente a classe, não é necessário corrigir multiplicação por 100
uso_solo_corrigido = uso_solo.astype(np.int32)

# Paleta categórica para visualização
cmap = plt.get_cmap("tab20", np.max(uso_solo_corrigido) + 1)

plt.figure(figsize=(12, 6))
plt.title("Uso e cobertura do solo (MapBiomas 2019)")
img = plt.imshow(uso_solo_corrigido, cmap=cmap)
plt.colorbar(img, ticks=np.unique(uso_solo_corrigido))
plt.grid(False)
plt.axis('off')
plt.show()

# Verificar valores únicos na imagem
print("Valores únicos encontrados:", np.unique(uso_solo_corrigido))

# Criar máscara booleana para áreas restauráveis
mascara_restauravel = np.isin(uso_solo_corrigido, classes_restauraveis).astype(np.uint8)

# === 4. Salvar a máscara como novo raster ===
perfil.update(dtype=rasterio.uint8, count=1)

with rasterio.open(saida_mascara, "w", **perfil) as dst:
    dst.write(mascara_restauravel, 1)

print("✅ Máscara salva como:", saida_mascara)

# === 5. Visualizar máscara final ===
plt.figure(figsize=(10, 5))
plt.title("Máscara de áreas restauráveis (1 = sim, 0 = não)")
plt.imshow(mascara_restauravel, cmap="gray_r", vmin=0, vmax=1)
plt.colorbar()
plt.show()

print("Total de pixels restauráveis:", np.sum(mascara_restauravel))

# Estatísticas por classe
valores, contagens = np.unique(uso_solo_corrigido, return_counts=True)
for v, c in zip(valores, contagens):
    print(f"Classe {v}: {c} pixels")
