# 192424059 - Assignment CO4-AT2

# Question 1 

# Warehouse Delivery Route Optimization
# Minimum Spanning Tree using Prim's Algorithm
#
# Concept:
# - Warehouse locations are vertices.
# - Route costs are edge weights.
# - MST connects all locations with minimum cost.
#
# Time Complexity: O(V²)
# Space Complexity: O(V)

print("\nQuestion 1 Output:\n")
def prim_mst(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True
    total_cost = 0
    print("Selected Routes:")
    for _ in range(n - 1):
        minimum = float('inf')
        x = y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x, y = i, j
        print(f"{x} -> {y} Cost = {graph[x][y]}")
        total_cost += graph[x][y]
        selected[y] = True
    print("Minimum Transportation Cost =", total_cost)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
prim_mst(graph)

# Question 2

# Manufacturing Resource Allocation
# Dynamic Programming - 0/1 Knapsack
#
# Goal:
# Maximize profit without exceeding budget.
#
# Time Complexity: O(nW)
# Space Complexity: O(nW)

print("\nQuestion 2 Output:\n")
products = ["A", "B", "C", "D"]
investment = [20, 30, 40, 50]  # in thousands
profit = [25, 40, 50, 65]      # in thousands
budget = 100
n = len(products)
dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(budget + 1):
        if investment[i - 1] <= w:
            dp[i][w] = max(
                profit[i - 1] + dp[i - 1][w - investment[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]
max_profit = dp[n][budget]
selected_products = []
w = budget
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_products.append(products[i - 1])
        w -= investment[i - 1]
selected_products.reverse()
print("Selected Products:", selected_products)
print("Maximum Profit =", max_profit * 1000)
print("\n")