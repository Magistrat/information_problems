from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Student:
    last_name: str  # Фамилия
    record_book_num: int  # Номер зачётной книжки
    height_cm: int  # Рост в сантиметрах


def counting_sort_students(students, key=lambda x: x.height_cm):
    if not students:
        return students

    # Получаем значения ключей для всех элементов
    keys = [key(student) for student in students]

    # Находим минимальное и максимальное значения ключей
    min_key = min(keys)
    max_key = max(keys)

    # Создаём массив для подсчёта частот и список для элементов
    count = [0] * (max_key - min_key + 1)
    output = [None] * len(students)

    # 1. Подсчитываем количество каждого ключа
    for k in keys:
        count[k - min_key] += 1

    # 2. Вычисляем начальные позиции для каждого ключа
    total = 0
    for i in range(len(count)):
        old_count = count[i]
        count[i] = total
        total += old_count

    # 3. Распределяем элементы по правильным позициям
    for student in students:
        k = key(student)
        output[count[k - min_key]] = student
        count[k - min_key] += 1

    return output


# Пример использования
if __name__ == "__main__":
    # Создаём массив студентов
    students = [
        Student("Иванов", 1001, 175),
        Student("Петров", 1002, 182),
        Student("Сидоров", 1003, 175),
        Student("Кузнецов", 1004, 168),
        Student("Смирнов", 1005, 182),
    ]

    print("Исходный массив студентов:")
    for student in students:
        print(f"{student.last_name:10} {student.record_book_num:4} {student.height_cm:3} см")

    # Сортируем по росту
    sorted_students = counting_sort_students(students)

    print("\nОтсортированный массив (по росту):")
    for student in sorted_students:
        print(f"{student.last_name:10} {student.record_book_num:4} {student.height_cm:3} см")
