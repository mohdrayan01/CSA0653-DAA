# Question 1 
print("\nQuestion 1 Output:\n")
def prim_mst(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True
    edge_count = 0
    total_weight = 0
    while edge_count < n - 1:
        minimum = float('inf')
        x = y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x, y = i, j
        print(f"Edge: {x} - {y}  Weight: {graph[x][y]}")
        total_weight += graph[x][y]
        selected[y] = True
        edge_count += 1
    print("Total weight =", total_weight)
graph = [
    [0, 2, 3],
    [2, 0, 1],
    [3, 1, 0]
]
prim_mst(graph)

# Question 2
print("\nQuestion 2 Output:\n")
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False
def kruskal(edges, vertices):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)
    mst_cost = 0
    print("Edges in MST:")
    for u, v, weight in edges:
        if ds.union(u, v):
            print(f"{u} - {v} : {weight}")
            mst_cost += weight
    print("MST Cost =", mst_cost)
edges = [
    (0, 1, 2),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 4),
    (2, 3, 5)
]
vertices = 4
kruskal(edges, vertices)
print("\n")
