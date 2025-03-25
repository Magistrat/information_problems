from collections import defaultdict, deque


def count_connected_components(edges):
    if not edges:
        return 0  # Если рёбер нет, каждая вершина — отдельная компонента (но в пустом графе 0 вершин)

    # Строим список смежности и находим все вершины
    graph = defaultdict(list)
    vertices = set()

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        vertices.add(u)
        vertices.add(v)

    visited = set()
    components = 0

    # Обходим все вершины
    for vertex in vertices:
        if vertex not in visited:
            # Запускаем BFS (можно заменить на DFS)
            queue = deque([vertex])
            visited.add(vertex)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            components += 1

    return components


if __name__ == '__main__':
    # Примеры использования
    edges1 = [(0, 1), (1, 2), (3, 4)]  # 2 компоненты: {0,1,2} и {3,4}
    print(count_connected_components(edges1))  # 2

    edges2 = [(0, 1), (1, 2), (2, 0), (3, 4)]  # 2 компоненты: {0,1,2} и {3,4}
    print(count_connected_components(edges2))  # 2

    edges3 = [(0, 1), (2, 3), (4, 5)]  # 3 компоненты: {0,1}, {2,3}, {4,5}
    print(count_connected_components(edges3))  # 3

    edges4 = []  # Пустой граф (0 компонент, т.к. нет вершин)
    print(count_connected_components(edges4))  # 0
