class ListNode:
    """Узел односвязного списка"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sort_linked_list(head):
    """
    Сортирует односвязный список с помощью сортировки слиянием

    Параметры:
        head: головной узел списка

    Возвращает:
        Отсортированный головной узел списка
    """
    # Базовый случай: пустой список или список из одного элемента
    if not head or not head.next:
        return head

    # Разделяем список на две половины
    left_half, right_half = split_list(head)

    # Рекурсивно сортируем каждую половину
    left_sorted = merge_sort_linked_list(left_half)
    right_sorted = merge_sort_linked_list(right_half)

    # Объединяем отсортированные половины
    return merge_lists(left_sorted, right_sorted)


def split_list(head):
    """
    Разделяет список на две половины с помощью метода "быстрый/медленный указатель"

    Параметры:
        head: головной узел списка

    Возвращает:
        Два головных узла для левой и правой половин
    """
    if not head:
        return None, None

    slow = head
    fast = head.next

    # Быстрый указатель движется в два раза быстрее медленного
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Разрываем список на две части
    right_half = slow.next
    slow.next = None

    return head, right_half


def merge_lists(left, right):
    """
    Объединяет два отсортированных списка в один

    Параметры:
        left: головной узел первого списка
        right: головной узел второго списка

    Возвращает:
        Головной узел объединенного отсортированного списка
    """
    dummy = ListNode()  # Фиктивный начальный узел
    tail = dummy

    while left and right:
        if left.val <= right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    # Присоединяем оставшиеся элементы
    tail.next = left if left else right

    return dummy.next


# Вспомогательная функция для создания списка из массива
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Вспомогательная функция для печати списка
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()


# Пример использования
if __name__ == "__main__":
    # Создаем тестовый список
    data = [12, 11, 13, 5, 6, 7, 1, -3, 0, 8]
    head = create_linked_list(data)

    print("Исходный список:")
    print_list(head)

    # Сортируем список
    sorted_head = merge_sort_linked_list(head)

    print("Отсортированный список:")
    print_list(sorted_head)
