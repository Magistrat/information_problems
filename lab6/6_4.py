import numpy as np
import timeit
import matplotlib.pyplot as plt
from typing import List


def radix_sort(arr: List[int], max_bits: int = 64) -> List[int]:
    """Поразрядная сортировка для unsigned long чисел"""
    if not arr:
        return arr

    # Определяем количество бит для сортировки
    bits = min(max_bits, 64)  # unsigned long - 64 бита

    for shift in range(bits):
        # Разделяем числа по текущему биту (начиная с младшего)
        zeros = []
        ones = []
        for num in arr:
            if (num >> shift) & 1 == 0:
                zeros.append(num)
            else:
                ones.append(num)
        arr = zeros + ones

    return arr


def generate_numbers(n: int, k_bits: int) -> List[int]:
    """Генерация n чисел с k значащими битами"""
    if k_bits < 64:
        max_val = (1 << k_bits) - 1
    else:
        max_val = (1 << 64) - 1  # Максимальное uint64 значение

    # Генерируем числа как uint64 и преобразуем в Python int
    return [int(x) for x in np.random.randint(0, max_val + 1, size=n, dtype=np.uint64)]


def measure_time(n_values: List[int], k_values: List[int], repeats: int = 3) -> np.ndarray:
    """Измерение времени выполнения для разных N и K"""
    results = np.zeros((len(n_values), len(k_values)))

    for i, n in enumerate(n_values):
        for j, k in enumerate(k_values):
            # Генерируем тестовые данные
            test_data = generate_numbers(n, k)

            # Измеряем время выполнения
            timer = timeit.Timer(lambda: radix_sort(test_data.copy(), k))
            time = timer.timeit(number=repeats) / repeats

            results[i, j] = time * 1000  # в миллисекундах

    return results


def plot_results(n_values: List[int], k_values: List[int], results: np.ndarray):
    """Визуализация результатов"""
    plt.figure(figsize=(14, 6))

    # График зависимости от N при разных K
    plt.subplot(1, 2, 1)
    for j, k in enumerate(k_values):
        plt.plot(n_values, results[:, j], 'o-', label=f'K={k}')
    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время (мс)')
    plt.title('Зависимость времени от N при разных K')
    plt.legend()
    plt.grid()

    # График зависимости от K при разных N
    plt.subplot(1, 2, 2)
    for i, n in enumerate(n_values[:4]):  # Показываем только первые 4 значения N для наглядности
        plt.plot(k_values, results[i, :], 's-', label=f'N={n}')
    plt.xlabel('Разрядность чисел (K)')
    plt.ylabel('Время (мс)')
    plt.title('Зависимость времени от K при разных N')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()


# Параметры исследования (уменьшены для быстрого выполнения)
n_values = [1000, 5000, 10000, 50000]  # Размеры массивов
k_values = [8, 16, 24, 32, 40, 48, 56, 64]  # Разрядности чисел

# Проводим измерения
print("Начинаем измерения...")
results = measure_time(n_values, k_values)

# Визуализируем результаты
plot_results(n_values, k_values, results)

# Выводим таблицу результатов
print("\nРезультаты (время в мс):")
print("N\K", end="")
for k in k_values:
    print(f"{k:8}", end="")
print()

for i, n in enumerate(n_values):
    print(f"{n:<6}", end="")
    for j in range(len(k_values)):
        print(f"{results[i, j]:8.2f}", end="")
    print()
