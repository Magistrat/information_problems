import numpy as np
import time


def traditional_multiply(A, B):
    m = A.shape[0]
    n = B.shape[1]
    C = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            C[i, j] = A[i, 0] * B[0, j]
    return C


def tiled_multiply(A, B, tile_size=32):
    m = A.shape[0]
    n = B.shape[1]
    C = np.zeros((m, n))

    for i in range(0, m, tile_size):
        for j in range(0, n, tile_size):
            # Обрабатываем блок [i:i+tile_size, j:j+tile_size]
            for ii in range(i, min(i + tile_size, m)):
                for jj in range(j, min(j + tile_size, n)):
                    C[ii, jj] = A[ii, 0] * B[0, jj]
    return C


def compare_methods(m, n):
    A = np.random.rand(m, 1)
    B = np.random.rand(1, n)

    # Традиционный метод
    start = time.time()
    C_trad = traditional_multiply(A, B)
    trad_time = time.time() - start

    # Мозаичный метод
    start = time.time()
    C_tiled = tiled_multiply(A, B, tile_size=32)
    tiled_time = time.time() - start

    # Проверка корректности
    assert np.allclose(C_trad, C_tiled)

    return trad_time, tiled_time


# Тестируем для разных размеров
sizes = [(100, 100), (500, 500), (1000, 1000), (3000, 3000)]
results = {}
for m, n in sizes:
    trad_time, tiled_time = compare_methods(m, n)
    results[(m, n)] = {
        'Традиционный (сек)': trad_time,
        'Мозаичный (сек)': tiled_time,
        'Ускорение': trad_time / tiled_time
    }

# Вывод результатов
print("Размер (m, n) | Традиционный | Мозаичный | Ускорение")
print("-------------|-------------|----------|----------")
for size, data in results.items():
    print(f"{size} | {data['Традиционный (сек)']:.5f} | {data['Мозаичный (сек)']:.5f} | {data['Ускорение']:.2f}x")
