def hanoi_4_rods(n, source, target, aux1, aux2):
    if n == 1:
        print(f"Переместить диск 1 с {source} на {target}")
        return
    if n == 2:
        print(f"Переместить диск 2 с {source} на {aux1}")
        print(f"Переместить диск 1 с {source} на {target}")
        print(f"Переместить диск 2 с {aux1} на {target}")
        return

    # Переносим (n-2) дисков на вспомогательные стержни
    hanoi_4_rods(n - 2, source, aux1, aux2, target)

    # Перемещаем 2 оставшихся диска на целевой стержень
    print(f"Переместить диск {n - 1} с {source} на {aux2}")
    print(f"Переместить диск {n} с {source} на {target}")
    print(f"Переместить диск {n - 1} с {aux2} на {target}")

    # Переносим (n-2) дисков с вспомогательных на целевой
    hanoi_4_rods(n - 2, aux1, target, source, aux2)


if __name__ == '__main__':
    print("Последовательность перемещений:")
    hanoi_4_rods(5, 'A', 'D', 'B', 'C')
    