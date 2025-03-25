class ListNode:
    """Узел односвязного списка"""

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def find_k_elements(head, k, find_max=True):
    """
    Находит K наибольших или наименьших элементов в односвязном списке

    Параметры:
        head: головной узел списка
        k: количество элементов для выборки
        find_max: если True - ищем наибольшие, False - наименьшие

    Возвращает:
        Список с K элементами
    """
    if not head or k <= 0:
        return []

    # Инициализируем список для хранения K элементов
    k_elements = []
    current = head

    # Заполняем начальными значениями
    while current and len(k_elements) < k:
        k_elements.append(current.value)
        current = current.next

    # Сортируем список в зависимости от того, ищем max или min
    k_elements.sort(reverse=find_max)

    # Обрабатываем оставшиеся элементы
    while current:
        current_val = current.value

        # Для поиска максимумов
        if find_max:
            if current_val > k_elements[-1]:
                k_elements.pop()
                # Вставляем элемент в правильную позицию
                for i in range(len(k_elements)):
                    if current_val > k_elements[i]:
                        k_elements.insert(i, current_val)
                        break
                else:
                    k_elements.append(current_val)
        # Для поиска минимумов
        else:
            if current_val < k_elements[-1]:
                k_elements.pop()
                # Вставляем элемент в правильную позицию
                for i in range(len(k_elements)):
                    if current_val < k_elements[i]:
                        k_elements.insert(i, current_val)
                        break
                else:
                    k_elements.append(current_val)

        current = current.next

    return k_elements


# Вспомогательная функция для создания списка из массива значений
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Пример использования
if __name__ == "__main__":
    # Создаем односвязный список
    values = [5, 3, 8, 1, 2, 7, 9, 4, 6]
    head = create_linked_list(values)

    k = 3
    print(f"Исходный список: {values}")
    print(f"{k} наибольших элементов: {find_k_elements(head, k, find_max=True)}")
    print(f"{k} наименьших элементов: {find_k_elements(head, k, find_max=False)}")
    