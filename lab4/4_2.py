import numpy as np
import time
import matplotlib.pyplot as plt


def quicksort(arr):
    """Рекурсивная реализация QuickSort (опорный — последний элемент)."""
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


def generate_array(n, alpha):
    """Генерация массива с степенью упорядоченности alpha."""
    sorted_part = int(n * alpha)
    random_part = n - sorted_part
    arr = np.concatenate((
        np.sort(np.random.randint(0, 100, sorted_part)),
        np.random.randint(0, 100, random_part)
    ))
    np.random.shuffle(arr)  # Для плавного перехода
    return arr

# Параметры эксперимента
n = 10000  # Размер массива
alphas = np.linspace(0, 1, 11)  # Степени упорядоченности от 0 до 1
runs = 10  # Количество запусков для усреднения

# Замер времени
times = []
for alpha in alphas:
    total_time = 0
    for _ in range(runs):
        arr = generate_array(n, alpha)
        start = time.time()
        quicksort(arr.copy())  # Копия, чтобы не менять исходный массив
        total_time += time.time() - start
    times.append(total_time / runs)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(alphas, times, marker='o', linestyle='-', color='b')
plt.title("Зависимость времени QuickSort от степени упорядоченности (α)")
plt.xlabel("Степень упорядоченности (α)")
plt.ylabel("Время выполнения (сек)")
plt.grid(True)
plt.show()
