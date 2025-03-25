import timeit
import random
from collections import deque


# Реализация простого односвязного списка
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


# Функция для измерения времени поиска
def measure_search_time(data_structure, elements_to_search):
    for element in elements_to_search:
        _ = element in data_structure  # Для list и deque
        # Для LinkedList используем метод find


# Параметры теста
size = 10000
test_iterations = 100
search_iterations = 100

# Создаем данные
test_data = list(range(size))
random.shuffle(test_data)

# Создаем структуры данных
regular_list = list(test_data)
deque_list = deque(test_data)
linked_list = LinkedList()
for item in test_data:
    linked_list.append(item)

# Элементы для поиска (первые, последние и случайные в середине)
search_elements = [
    test_data[0],  # первый элемент
    test_data[size // 2],  # элемент в середине
    test_data[-1],  # последний элемент
    -1  # отсутствующий элемент
]

# Тестирование стандартного списка (list)
list_time = timeit.timeit(
    lambda: measure_search_time(regular_list, search_elements),
    number=test_iterations
)

# Тестирование deque
deque_time = timeit.timeit(
    lambda: measure_search_time(deque_list, search_elements),
    number=test_iterations
)


# Тестирование LinkedList
def linked_list_search():
    for element in search_elements:
        linked_list.find(element)


linked_list_time = timeit.timeit(
    linked_list_search,
    number=test_iterations
)

# Вывод результатов
print(f"Результаты для {size} элементов (в секундах за {test_iterations} итераций):")
print(f"Стандартный список (list): {list_time:.5f}")
print(f"Deque (двусвязный список): {deque_time:.5f}")
print(f"Односвязный список (LinkedList): {linked_list_time:.5f}")
