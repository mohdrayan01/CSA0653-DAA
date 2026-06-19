# 192424059 - Assignment CO3-AT1
# Question 1
print("Question 1 Output:")
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted Array:", arr, "\n")

# Question 2 
print("Question 2 Output:")
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, count
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, count
arr = list(range(1, 101))
index, iterations = binary_search(arr, 85)
print("Position:", index)
print("Iterations:", iterations, "\n")
