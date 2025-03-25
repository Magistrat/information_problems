def print_pythagorean_triples(N, c=5, found_triples=None):
    if found_triples is None:
        found_triples = set()

    if c > N // 2:
        return

    # Перебираем b от 1 до c-1
    for b in range(1, c):
        # Перебираем a от 1 до b
        for a in range(1, b):
            perimeter = a + b + c
            if perimeter > N:
                continue  # Пропускаем, если периметр превышает N
            if a ** 2 + b ** 2 == c ** 2:
                triple = tuple(sorted((a, b, c)))
                if triple not in found_triples:
                    found_triples.add(triple)
                    print(f"({a}, {b}, {c}) | Периметр = {perimeter}")

    print_pythagorean_triples(N, c + 1, found_triples)


if __name__ == '__main__':
    N = 100
    print(f"Пифагоровы тройки с периметром ≤ {N}:")
    print_pythagorean_triples(N)
