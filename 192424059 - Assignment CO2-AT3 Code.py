# 192424059 - Assignment CO2-AT3
# Question 1
print("Question 1 Output:\n")
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)
print("Sorted Array:", selection_sort(arr))
print("\n")

# Question 2
print("Question 2 Output:\n")
def string_match(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")
result = string_match(text, pattern)
if result != -1:
    print("Pattern found at index:", result)
else:
    print("Pattern not found")
print("\n")
