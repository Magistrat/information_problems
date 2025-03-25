from copy import copy
from typing import List, Any


a = [1, 2, 3, -1, 4, 3]


def delete_item(array: List, index: int) -> List:
    c_array = copy(array)
    c_array.pop(index)
    return c_array


def insert_item(array: List, index: int, item: Any) -> List:
    return array[:index] + [item] + array[index:]


if __name__ == '__main__':
    print(a)
    print('delete_item', delete_item(a, 1))
    print('insert_item', insert_item(a, 1, 'a'))
    print(a)
