import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
file_path = 'Desktop/cosmos/spot6.tif'  # Замените на путь к вашему файлу TIFF

with rasterio.open(file_path) as src:
    red_band = src.read(1)  # Красный канал
    nir_band = src.read(4)  # Ближний инфракрасный канал (предположим, что это 4-й канал)

# Расчет NDVI
ndvi = (nir_band - red_band) / (nir_band + red_band)

# Определение процента зелени
# NDVI значения обычно варьируются от -1 до 1. Значения ближе к 1 указывают на высокую растительность.
# Предположим, что значения NDVI выше 0.3 указывают на зелень.
green_threshold = 0.3
green_pixels = np.sum(ndvi > green_threshold)
total_pixels = ndvi.size
green_percentage = (green_pixels / total_pixels) * 100

print(f'Percentage of land covered by green: {green_percentage:.2f}%')

# Визуализация NDVI
plt.figure(figsize=(10, 6))
plt.imshow(ndvi, cmap='viridis')
plt.colorbar(label='NDVI')
plt.title('NDVI Map')
plt.show()
