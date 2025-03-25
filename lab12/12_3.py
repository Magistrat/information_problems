class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False  # Уже в одном множестве → цикл
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True


def kruskal_mst(edges, num_vertices):
    edges_sorted = sorted(edges, key=lambda x: x[2])  # Сортировка по весу (если есть)
    dsu = DSU(num_vertices)
    mst = []

    for u, v, weight in edges_sorted:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:
                break
    return mst


if __name__ == '__main__':
    # Пример использования (взвешенный граф)
    edges = [
        (0, 1, 2), (1, 2, 3), (0, 2, 1), (1, 3, 4), (2, 3, 5)
    ]
    num_vertices = 4

    mst = kruskal_mst(edges, num_vertices)
    print("Остовное дерево (рёбра):", mst)
