import numpy as np
import time
import random
import matplotlib.pyplot as plt

def quicksort_fixed(arr):
    """QuickSort с фиксированным pivot (последний элемент)."""
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort_fixed(left) + [pivot] + quicksort_fixed(right)

def quicksort_random(arr):
    """QuickSort со случайным pivot."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_random(left) + [pivot] * arr.count(pivot) + quicksort_random(right)

def quicksort_median3(arr):
    """QuickSort с медианой трёх в качестве pivot."""
    if len(arr) <= 1:
        return arr
    # Выбираем медиану среди первого, среднего и последнего элементов
    candidates = [arr[0], arr[len(arr)//2], arr[-1]]
    pivot = sorted(candidates)[1]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_median3(left) + [pivot] * arr.count(pivot) + quicksort_median3(right)

def quicksort_external_pivot(arr):
    """QuickSort с pivot вне массива (среднее арифметическое)."""
    if len(arr) <= 1:
        return arr
    pivot = sum(arr) / len(arr)  # Pivot может не принадлежать массиву!
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_external_pivot(left) + [x for x in arr if x == pivot] + quicksort_external_pivot(right)

# Сравнение методов
def test_pivot_strategy(strategy, arr):
    start = time.time()
    strategy(arr.copy())
    return time.time() - start

# Параметры теста
n = 100  # Размер массива
arr_random = np.random.randint(0, 100, n)
arr_sorted = np.sort(arr_random)
arr_reversed = arr_sorted[::-1]

strategies = {
    "Фиксированный (последний)": quicksort_fixed,
    "Случайный": quicksort_random,
    "Медиана трёх": quicksort_median3,
    "Внешний pivot (среднее)": quicksort_external_pivot
}

results = {}
for name, strategy in strategies.items():
    times = {
        "Случайный массив": test_pivot_strategy(strategy, arr_random),
        "Отсортированный массив": test_pivot_strategy(strategy, arr_sorted),
        "Обратно отсортированный": test_pivot_strategy(strategy, arr_reversed)
    }
    results[name] = times

# Визуализация
fig, ax = plt.subplots(figsize=(12, 6))
x = np.arange(len(results))
width = 0.25

for i, (condition, color) in enumerate(zip(
    ["Случайный массив", "Отсортированный массив", "Обратно отсортированный"],
    ["blue", "green", "red"]
)):
    ax.bar(
        x + i * width,
        [results[strategy][condition] for strategy in strategies],
        width,
        label=condition,
        color=color
    )

ax.set_xticks(x + width)
ax.set_xticklabels(strategies.keys())
ax.set_ylabel("Время (сек)")
ax.set_title("Сравнение методов выбора pivot в QuickSort")
ax.legend()
plt.show()
