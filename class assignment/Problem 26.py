def median(arr):
    arr.sort()
    n = len(arr)
    
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


# Example 1
arr1 = [90, 100, 78, 89, 67]
print("Median:", median(arr1))

# Example 2
arr2 = [56, 67, 30, 79]
print("Median:", median(arr2))
    
