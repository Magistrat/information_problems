from typing import List


def binary_search(arr: List, target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    targ = 7

    print(binary_search(sorted_array, targ))
    print(binary_search(sorted_array, 8))
