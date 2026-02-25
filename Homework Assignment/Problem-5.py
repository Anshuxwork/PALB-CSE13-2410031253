def largest_element(arr):
    maximum = arr[0]
    
    for num in arr:
        if num > maximum:
            maximum = num
            
    return maximum

# Example
arr = [1, 8, 7, 56, 90]
print(largest_element(arr))