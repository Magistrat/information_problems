import numpy as np


def strassen_multiply(A, B):
    n = len(A)

    # Базовый случай: матрицы 1x1
    if n == 1:
        return A * B

    # Разбиваем матрицы на подматрицы
    half = n // 2
    A11 = A[:half, :half]
    A12 = A[:half, half:]
    A21 = A[half:, :half]
    A22 = A[half:, half:]

    B11 = B[:half, :half]
    B12 = B[:half, half:]
    B21 = B[half:, :half]
    B22 = B[half:, half:]

    # Вычисляем промежуточные матрицы M1-M7
    M1 = strassen_multiply(A11 + A22, B11 + B22)
    M2 = strassen_multiply(A21 + A22, B11)
    M3 = strassen_multiply(A11, B12 - B22)
    M4 = strassen_multiply(A22, B21 - B11)
    M5 = strassen_multiply(A11 + A12, B22)
    M6 = strassen_multiply(A21 - A11, B11 + B12)
    M7 = strassen_multiply(A12 - A22, B21 + B22)

    # Собираем результирующую матрицу
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Объединяем подматрицы в одну
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C


# Пример использования
n = 4  # 2^2 = 4
A = np.random.randint(0, 10, (n, n))
B = np.random.randint(0, 10, (n, n))

print("Матрица A:\n", A)
print("Матрица B:\n", B)

C = strassen_multiply(A, B)
print("Результат умножения (Штрассен):\n", C)

# Проверка корректности через numpy
C_np = np.dot(A, B)
print("Результат через np.dot:\n", C_np)
print("Совпадает с numpy?:", np.allclose(C, C_np))
