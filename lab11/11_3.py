def print_undirected_graph_info(graph):
    """
    Выводит информацию о всех вершинах неориентированного графа:
    - Имя вершины
    - Координаты (x, y)
    - Список смежных вершин
    """
    for node_name, node_data in graph.items():
        x, y = node_data["coords"]
        adjacent_nodes = node_data["edges"]

        print(f"Вершина: {node_name}")
        print(f"  Координаты: ({x}, {y})")
        print(f"  Смежные вершины: {', '.join(adjacent_nodes) if adjacent_nodes else 'нет'}")
        print()  # Пустая строка для разделения


if __name__ == '__main__':
    # Пример использования:
    graph = {
        "A": {"coords": (0, 0), "edges": {"B", "C"}},
        "B": {"coords": (1, 2), "edges": {"A", "D"}},
        "C": {"coords": (2, 1), "edges": {"A", "D", "E"}},
        "D": {"coords": (3, 3), "edges": {"B", "C"}},
        "E": {"coords": (4, 0), "edges": {"C"}},
    }

    print_undirected_graph_info(graph)
