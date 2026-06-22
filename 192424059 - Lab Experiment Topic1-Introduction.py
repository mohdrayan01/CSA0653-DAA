# Question 1 
print("Question 1")
words = ["abc", "car", "ada", "racecar", "cool"]
answer = ""
for word in words:
    if word == word[::-1]:
        answer = word
        break
print(answer+"\n")

# Question 2
print("Question 2")
nums1 = [2, 3, 2]
nums2 = [1, 2]
answer1 = 0
answer2 = 0
for x in nums1:
    if x in nums2:
        answer1 += 1
for x in nums2:
    if x in nums1:
        answer2 += 1
print([answer1, answer2], "\n")

# Question 3    
print("Question 3")
nums = [1, 2, 1]
total = 0
for i in range(len(nums)):
    s = set()
    for j in range(i, len(nums)):
        s.add(nums[j])
        total += len(s) ** 2
print(total, "\n")

# Question 4
print("Question 4")
nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and (i * j) % k == 0:
            count += 1
print(count, "\n")

# Question 5
print("Question 5")
arr = [1, 2, 3, 4, 5]
maximum = arr[0]
for i in arr:
    if i > maximum:
        maximum = i
print(maximum, "\n")

# Question 6
print("Question 6")
arr = [12, 5, 8, 3]
if len(arr) == 0:
    print("Empty List")
else:
    arr.sort()
    print(arr[-1], "\n")

# Question 7
print("Question 7")
arr = [3, 7, 3, 5, 2, 5, 9, 2]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique, "\n")

# Question 8
print("Question 8")
arr = [5, 2, 9, 1, 5, 6]
n = len(arr)
for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr, "\n")

# Question 9
print("Question 9")
arr = [3, 4, 6, -9, 10, 8, 9, 30]
key = 10
arr.sort()
low = 0
high = len(arr) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
print("\n")
if not found:
    print("Element not found", "\n")

# Question 10
print("Question 10")
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
arr = [5, 2, 3, 1]
print("Sorted Array:", merge_sort(arr), "\n")

# Question 11
print("Question 11")
def find_paths(m, n, N, row, col):
    if row < 0 or row >= m or col < 0 or col >= n:
        return 1
    if N == 0:
        return 0
    return (
        find_paths(m, n, N - 1, row + 1, col) +
        find_paths(m, n, N - 1, row - 1, col) +
        find_paths(m, n, N - 1, row, col + 1) +
        find_paths(m, n, N - 1, row, col - 1)
    )
print(find_paths(2, 2, 2, 0, 0), "\n")

#Question 12
print("Question 12")
def rob(nums):
    if len(nums) == 1:
        return nums[0]
    def helper(arr):
        prev = 0
        curr = 0
        for num in arr:
            temp = max(curr, prev + num)
            prev = curr
            curr = temp
        return curr
    return max(helper(nums[:-1]), helper(nums[1:]))
nums = [2, 3, 2]
print("Maximum Money:", rob(nums), "\n")

#Question 13
print("Question 13")
def climb_stairs(n):
    if n <= 2:
        return n
    a = 1
    b = 2
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b
print(climb_stairs(4), "\n")

# Question 14
print("Question 14")
def unique_paths(m, n):
    dp = [[1 for j in range(n)] for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
print(unique_paths(7, 3), "\n")

# Question 15
print("Question 15")
def large_group_positions(s):
    result = []
    start = 0
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            if i - start + 1 >= 3:
                result.append([start, i])
            start = i + 1
    return result
s = "abbxxxxzzy"
print(large_group_positions(s), "\n")

# Question 16
print("Question 16")
def game_of_life(board):
    rows = len(board)
    cols = len(board[0])
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)
    ]
    new_board = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            live = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    live += board[nr][nc]
            if board[r][c] == 1:
                if live == 2 or live == 3:
                    new_board[r][c] = 1
            else:
                if live == 3:
                    new_board[r][c] = 1
    return new_board
board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]
print(game_of_life(board), "\n")

# Question 17
print("Question 17")
def champagne_tower(poured, query_row, query_glass):
    tower = [[0.0] * 101 for _ in range(101)]
    tower[0][0] = poured
    for row in range(100):
        for glass in range(row + 1):
            extra = (tower[row][glass] - 1.0) / 2.0
            if extra > 0:
                tower[row + 1][glass] += extra
                tower[row + 1][glass + 1] += extra
    return min(1, tower[query_row][query_glass])
print(champagne_tower(2, 1, 1))