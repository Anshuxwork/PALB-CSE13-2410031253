def chocolate_distribution(arr, m):
    if m == 0 or len(arr) < m:
        return 0
    
    arr.sort()
    min_diff = float('inf')
    
    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    
    return min_diff

# Example
arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(chocolate_distribution(arr, m))