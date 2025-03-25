def counting_sort(arr):
    if not arr:
        return arr

    # Находим минимальное и максимальное значения в массиве
    min_val = min(arr)
    max_val = max(arr)

    # Создаём массив для подсчёта частот
    count = [0] * (max_val - min_val + 1)

    # Подсчитываем количество каждого элемента
    for num in arr:
        count[num - min_val] += 1

    # Восстанавливаем отсортированный массив
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr


# Пример использования
if __name__ == "__main__":
    # Тестовый массив
    numbers = [4, 2, 2, 8, 3, 3, 1, -5, 0, 2]
    print("Исходный массив:", numbers)

    # Сортируем массив
    sorted_numbers = counting_sort(numbers)
    print("Отсортированный массив:", sorted_numbers)
    