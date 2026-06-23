# Question 1 
print("\nQuestion 1 Output:\n")
investments = ['A', 'B', 'C', 'D']
capital = [20000, 30000, 40000, 50000]
returns = [25000, 40000, 50000, 70000]
budget = 80000
print("Greedy Approach")
items = []
for i in range(len(investments)):
    ratio = returns[i] / capital[i]
    items.append((ratio, investments[i], capital[i], returns[i]))
items.sort(reverse=True)
selected = []
total_capital = 0
total_return = 0
for ratio, name, cost, profit in items:
    if total_capital + cost <= budget:
        selected.append(name)
        total_capital += cost
        total_return += profit
print("Selected Investments:", selected)
print("Capital Used:", total_capital)
print("Total Return:", total_return)
print("\nDynamic Programming Approach")
n = len(investments)
weights = [c // 1000 for c in capital]
capacity = budget // 1000
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                returns[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]
max_return = dp[n][capacity]
selected_items = []
w = capacity
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(investments[i - 1])
        w -= weights[i - 1]
selected_items.reverse()
print("Selected Investments:", selected_items)
print("Maximum Return:", max_return)

# Question 2
print("\nQuestion 2 Output:\n")
packages = ["P1", "P2", "P3", "P4"]
weights = [10, 20, 30, 25]
profits = [60, 100, 120, 110]
capacity = 50
print("Greedy Approach")
items = []
for i in range(len(packages)):
    ratio = profits[i] / weights[i]
    items.append((ratio, packages[i], weights[i], profits[i]))
items.sort(reverse=True)
selected = []
total_weight = 0
total_profit = 0
for ratio, name, wt, prof in items:
    if total_weight + wt <= capacity:
        selected.append(name)
        total_weight += wt
        total_profit += prof
print("Selected Packages:", selected)
print("Total Weight:", total_weight)
print("Total Profit:", total_profit)
print("\nDynamic Programming Approach")
n = len(packages)
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]
max_profit = dp[n][capacity]
selected_packages = []
w = capacity
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_packages.append(packages[i - 1])
        w -= weights[i - 1]
selected_packages.reverse()
print("Selected Packages:", selected_packages)
print("Maximum Profit:", max_profit)
print("\n")