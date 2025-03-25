import time


def solve_n_queens(n):
    def is_safe(board, row, col):
        # Проверка вертикали и диагоналей
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row, board):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    solutions = []
    board = [-1] * n
    backtrack(0, board)
    return solutions


# Измерение времени выполнения
def measure_time(n):
    start_time = time.time()
    solutions = solve_n_queens(n)
    end_time = time.time()
    return len(solutions), end_time - start_time

# Анализ для n от 4 до 12
results = {}
for n in range(4, 13):
    count, time_taken = measure_time(n)
    results[n] = {
        "Количество решений": count,
        "Время (сек)": round(time_taken, 4),
        "Чётность": "чётное" if n % 2 == 0 else "нечётное"
    }

# Вывод результатов
print("n | Решений | Время (сек) | Чётность")
print("--|---------|------------|---------")
for n, data in results.items():
    print(f"{n} | {data['Количество решений']:7} | {data['Время (сек)']:10} | {data['Чётность']}")
