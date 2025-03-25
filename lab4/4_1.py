import numpy as np
import random


def generate_array(size, alpha, ascending=True):
    """
    Генерирует массив с заданной степенью упорядоченности.

    :param size: Размер массива.
    :param alpha: Степень упорядоченности (0 ≤ α ≤ 1).
    :param ascending: Если True, сортировка по возрастанию, иначе по убыванию.
    :return: Сгенерированный массив.
    """
    if alpha == 0:
        return np.random.randint(0, 100, size)
    elif alpha == 1:
        arr = np.random.randint(0, 100, size)
        return np.sort(arr) if ascending else np.sort(arr)[::-1]
    else:
        # Часть массива оставляем упорядоченной, остальное перемешиваем
        sorted_part = int(size * alpha)
        random_part = size - sorted_part

        # Генерируем упорядоченную часть
        sorted_arr = np.random.randint(0, 100, sorted_part)
        sorted_arr = np.sort(sorted_arr) if ascending else np.sort(sorted_arr)[::-1]

        # Генерируем случайную часть
        random_arr = np.random.randint(0, 100, random_part)

        # Объединяем и перемешиваем границу для плавного перехода
        combined = np.concatenate((sorted_arr, random_arr))
        np.random.shuffle(combined[sorted_part - 1: sorted_part + 1])  # Сглаживаем стык

        return combined


# Пример использования
size = 10
alpha = 0.7  # 70% упорядоченности
arr = generate_array(size, alpha, ascending=True)
print("Сгенерированный массив:", arr)


def calculate_disorder(arr):
    """Вычисляет степень неупорядоченности (0 ≤ β ≤ 1)."""
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    max_inversions = n * (n - 1) / 2
    return inversions / max_inversions  # β ≈ 1 - α

# Проверка
beta = calculate_disorder(arr)
print(f"Степень неупорядоченности (β): {beta:.2f}")
print(f"Фактическая упорядоченность (α ≈ {1 - beta:.2f})")