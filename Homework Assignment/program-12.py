def minimize_heights(arr, k):
    n = len(arr)
    arr.sort()
    
    ans = arr[-1] - arr[0]
    small = arr[0] + k
    big = arr[-1] - k
    
    if small > big:
        small, big = big, small
    
    for i in range(1, n-1):
        subtract = arr[i] - k
        add = arr[i] + k
        
        if subtract >= small or add <= big:
            continue
        
        if big - subtract <= add - small:
            small = subtract
        else:
            big = add
    
    return min(ans, big - small)

# Example
arr = [1, 5, 8, 10]
k = 2
print(minimize_heights(arr, k))