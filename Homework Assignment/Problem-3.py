def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]

# Example
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
print(kth_smallest(arr, k))