import timeit
import numpy as np
import matplotlib.pyplot as plt


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def generate_array(n, ordered_percent=0):
    arr = np.random.rand(n)
    if ordered_percent > 0:
        k = int(n * ordered_percent)
        arr[:k] = np.sort(arr[:k])
    return arr


sizes = [100, 1000, 5000, 10000, 20000]
ordered_percents = [0, 0.25, 0.5, 0.75, 1.0]

results = {p: [] for p in ordered_percents}

for size in sizes:
    for p in ordered_percents:
        arr = generate_array(size, p)
        time = timeit.timeit(lambda: heapsort(arr.copy()), number=10)
        results[p].append(time)

# Построение графиков
plt.figure(figsize=(10, 6))
for p in ordered_percents:
    plt.plot(sizes, results[p], label=f"Упорядоченность {int(p*100)}%")

plt.xlabel("Размер массива")
plt.ylabel("Время (сек)")
plt.title("Зависимость времени Heapsort от размера и упорядоченности")
plt.legend()
plt.grid()
plt.show()
