class ListNode:
    """Узел односвязного списка"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def heap_sort_linked_list(head):
    """
    Сортирует односвязный список с помощью пирамидальной сортировки

    Параметры:
        head: головной узел списка

    Возвращает:
        Отсортированный головной узел списка
    """
    if not head or not head.next:
        return head

    # Преобразуем список в массив для удобства работы с кучей
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next

    # Реализация пирамидальной сортировки
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

    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    # Создаем новый отсортированный список
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next

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
    data = [12, 11, 13, 5, 6, 7]
    head = create_linked_list(data)

    print("Исходный список:")
    print_list(head)

    # Сортируем список
    sorted_head = heap_sort_linked_list(head)

    print("Отсортированный список:")
    print_list(sorted_head)
