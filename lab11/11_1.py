import math


def euclidean_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


if __name__ == '__main__':
    # Пример:
    A = (0, 0)
    B = (3, 4)
    print(euclidean_distance(A, B))  # 5.0
