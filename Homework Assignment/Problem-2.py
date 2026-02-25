def find_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]
    
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    return [minimum, maximum]

# Example
arr = [1, 4, 3, 5, 8, 6]
print(find_min_max(arr))