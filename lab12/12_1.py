from collections import defaultdict


def is_tree(edges):
    if not edges:
        return True  # Пустой граф считается деревом (0 вершин, 0 рёбер)

    # Строим список смежности
    graph = defaultdict(list)
    vertices = set()

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        vertices.add(u)
        vertices.add(v)

    V = len(vertices)
    E = len(edges)

    # Проверка первого условия: E = V - 1
    if E != V - 1:
        return False

    # Проверка связности через DFS
    visited = set()
    stack = [next(iter(vertices))]  # Начинаем с первой вершины

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    # Если все вершины посещены, граф связный
    return len(visited) == V


if __name__ == '__main__':
    # Пример использования
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]  # Дерево
    print(is_tree(edges))  # True

    edges_with_cycle = [(0, 1), (1, 2), (2, 0)]  # Граф с циклом
    print(is_tree(edges_with_cycle))  # False

    disconnected_graph = [(0, 1), (2, 3)]  # Несвязный граф
    print(is_tree(disconnected_graph))  # False
