from collections import deque


def bfs(graph, start_node):
    """
    Итеративный BFS с использованием очереди.
    :param graph: словарь, представляющий граф
    :param start_node: начальная вершина
    :return: список посещённых вершин в порядке обхода
    """
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        print(f"Посещена вершина: {node} (координаты: {graph[node]['coords']})")

        for neighbor in graph[node]["edges"]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


if __name__ == '__main__':
    # Пример использования:
    graph = {
        "A": {"coords": (0, 0), "edges": {"B", "C"}},
        "B": {"coords": (1, 2), "edges": {"A", "D"}},
        "C": {"coords": (2, 1), "edges": {"A", "D", "E"}},
        "D": {"coords": (3, 3), "edges": {"B", "C"}},
        "E": {"coords": (4, 0), "edges": {"C"}},
    }

    print("BFS обход графа:")
    bfs_order = bfs(graph, "A")
