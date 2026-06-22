# Question 1
print("Question 1")
arr = [-5, -1, -3, -2, -4]
n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr, "\n")

# Question 2
print("Question 2")
arr = [5, 2, 9, 1, 5, 6]
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Sorted Array:", arr, "\n")

# Question 3
print("Question 3")
arr = [64, 25, 12, 22, 11]
n = len(arr)
for i in range(n):
    swapped = False
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break
print("Sorted Array:", arr, "\n")

# Question 4
print("Question 4")
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print("Sorted Array:", arr, "\n")

# Question 5
print("Question 5")
arr = [2, 3, 4, 7, 11]
k = 5
current = 1
missing = 0
i = 0
while missing < k:
    if i < len(arr) and arr[i] == current:
        i += 1
    else:
        missing += 1
        if missing == k:
            print("Answer:", current)
            break
    current += 1
print()

# Question 6
print("Question 6")
nums = [1, 2, 3, 1]
peak = -1
for i in range(len(nums)):
    left = float('-inf') if i == 0 else nums[i - 1]
    right = float('-inf') if i == len(nums) - 1 else nums[i + 1]
    if nums[i] > left and nums[i] > right:
        peak = i
        break
print("Peak Index:", peak, "\n")

# Question 7
print("Question 7")
haystack = "sadbutsad"
needle = "sad"
answer = haystack.find(needle)
print("Index:", answer, "\n")

# Question 8
print("Question 8")
words = ["mass", "as", "hero", "superhero"]
result = []
for i in range(len(words)):
    for j in range(len(words)):
        if i != j and words[i] in words[j]:
            if words[i] not in result:
                result.append(words[i])
print(result, "\n")

# Question 9
print("Question 9")
points = [(1, 2), (4, 5), (7, 8), (3, 1)]
min_distance = float('inf')
closest_pair = ()
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_pair = (points[i], points[j])
print("Closest Pair:", closest_pair)
print("Minimum Distance:", min_distance, "\n")

# Question 10
print("Question 10")
points = [(1,1), (4,6), (8,1), (0,0), (3,3)]
hull = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        a = points[i]
        b = points[j]
        pos = neg = 0
        for k in range(len(points)):
            if k == i or k == j:
                continue
            c = points[k]
            value = ((b[0] - a[0]) * (c[1] - a[1]) -
                     (b[1] - a[1]) * (c[0] - a[0]))
            if value > 0:
                pos += 1
            elif value < 0:
                neg += 1
        if pos == 0 or neg == 0:
            if a not in hull:
                hull.append(a)
            if b not in hull:
                hull.append(b)
print("Convex Hull:", hull)
print()

# Question 11
print("Question 11")
points = [(1,1), (4,6), (8,1), (0,0), (3,3)]
hull = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        pos = 0
        neg = 0
        for k in range(len(points)):
            if k == i or k == j:
                continue
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            value = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            if value > 0:
                pos += 1
            elif value < 0:
                neg += 1
        if pos == 0 or neg == 0:
            if points[i] not in hull:
                hull.append(points[i])
            if points[j] not in hull:
                hull.append(points[j])
print("Convex Hull:", hull)
print()

# Question 12
print("Question 12")
from itertools import permutations
cities = [(1,2), (4,5), (7,1), (3,6)]
min_distance = float('inf')
best_path = None
for path in permutations(range(1, len(cities))):
    route = (0,) + path + (0,)
    distance = 0
    for i in range(len(route) - 1):
        x1, y1 = cities[route[i]]
        x2, y2 = cities[route[i + 1]]
        distance += ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    if distance < min_distance:
        min_distance = distance
        best_path = route
print("Shortest Distance:", min_distance)
print("Best Path:", best_path)
print()

# Question 13
print("Question 13")
from itertools import permutations
cost = [
    [3,10,7],
    [8,5,12],
    [4,6,9]
]
n = len(cost)
min_cost = float('inf')
best_assignment = None
for perm in permutations(range(n)):
    total = 0
    for worker in range(n):
        total += cost[worker][perm[worker]]
    if total < min_cost:
        min_cost = total
        best_assignment = perm
print("Optimal Assignment:", best_assignment)
print("Minimum Cost:", min_cost)
print()

# Question 14
print("Question 14")
weights = [2, 3, 1]
values = [4, 5, 3]
capacity = 4
best_value = 0
best_items = []
n = len(weights)
for mask in range(1 << n):
    total_weight = 0
    total_value = 0
    selected = []
    for i in range(n):
        if mask & (1 << i):
            total_weight += weights[i]
            total_value += values[i]
            selected.append(i)
    if total_weight <= capacity and total_value > best_value:
        best_value = total_value
        best_items = selected
print("Selected Items:", best_items)
print("Maximum Value:", best_value)
print()