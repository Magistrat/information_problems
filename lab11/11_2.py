def print_graph_info(graph):
    """
    Выводит информацию о всех вершинах графа:
    - Имя вершины
    - Координаты (x, y)
    - Список вершин, в которые можно перейти
    """
    for node_name, node_data in graph.items():
        coords = node_data["coords"]
        edges = node_data["edges"]

        print(f"Вершина: {node_name}")
        print(f"  Координаты: ({coords[0]}, {coords[1]})")
        print(f"  Можно перейти в: {', '.join(edges) if edges else 'нет'}")
        print()  # Пустая строка для разделения


if __name__ == '__main__':
    # Пример использования:
    graph = {
        "A": {"coords": (0, 0), "edges": ["B", "C"]},
        "B": {"coords": (1, 2), "edges": ["D"]},
        "C": {"coords": (2, 1), "edges": ["D", "E"]},
        "D": {"coords": (3, 3), "edges": []},
        "E": {"coords": (4, 0), "edges": ["A"]},
    }

    print_graph_info(graph)
