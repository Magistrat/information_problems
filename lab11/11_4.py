def dfs(graph, start_node, visited=None):
    """
    Рекурсивный обход графа в глубину.
    :param graph: словарь, представляющий граф
    :param start_node: начальная вершина
    :param visited: множество посещённых вершин (None при первом вызове)
    :return: множество посещённых вершин
    """
    if visited is None:
        visited = set()

    visited.add(start_node)
    print(f"Посещена вершина: {start_node} (координаты: {graph[start_node]['coords']})")

    for neighbor in graph[start_node]["edges"]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


if __name__ == '__main__':
    # Пример использования:
    graph = {
        "A": {"coords": (0, 0), "edges": {"B", "C"}},
        "B": {"coords": (1, 2), "edges": {"A", "D"}},
        "C": {"coords": (2, 1), "edges": {"A", "D", "E"}},
        "D": {"coords": (3, 3), "edges": {"B", "C"}},
        "E": {"coords": (4, 0), "edges": {"C"}},
    }

    print("Рекурсивный DFS обход:")
    dfs(graph, "A")
