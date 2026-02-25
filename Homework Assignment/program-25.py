def min_swaps(arr, k):
    n = len(arr)
    count = sum(1 for num in arr if num <= k)
    
    bad = sum(1 for num in arr[:count] if num > k)
    min_swaps = bad
    
    for i in range(count, n):
        if arr[i - count] > k:
            bad -= 1
        if arr[i] > k:
            bad += 1
        min_swaps = min(min_swaps, bad)
    
    return min_swaps