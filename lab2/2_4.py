from typing import Tuple, Any


a = [1, 2, 3, -1, 4, 3]


def find_item(array: Tuple, item: Any) -> int:
    for element_index, element in enumerate(array):
        if element == item:
            return element_index

    return -1


if __name__ == '__main__':
    print(a)
    print('find_item 1', find_item(a, 1))
    print('find_item 10', find_item(a, 10))
    print('find_item 3', find_item(a, 3))
    print('find_item 4', find_item(a, 4))
