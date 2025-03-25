def print_permutations(arr, start=0):
    if start == len(arr) - 1:
        print(arr)
    else:
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            print_permutations(arr, start + 1)
            arr[start], arr[i] = arr[i], arr[start]


if __name__ == '__main__':
    array = [1, 2, 3]
    print_permutations(array)
