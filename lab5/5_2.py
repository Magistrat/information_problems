import timeit
import numpy as np
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


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
        time = timeit.timeit(lambda: merge_sort(arr.copy()), number=10)
        results[p].append(time)

plt.figure(figsize=(10, 6))
for p in ordered_percents:
    plt.plot(sizes, results[p], label=f"Упорядоченность {int(p * 100)}%")

plt.xlabel("Размер массива")
plt.ylabel("Время (сек)")
plt.title("Зависимость времени Merge Sort от размера и упорядоченности")
plt.legend()
plt.grid()
plt.show()
