def min_height(arr,k):
    n = len (arr)
    arr.sort()

    #initial difference
    result = arr[-1] - arr[0]
    small = arr[0] + k
    big = arr[-1] - k

#smaller tower will always smaller
#small < big
    if small > big:
        small, big = big, small

    for i in range(1,n):
        subtract = arr[i] - k
        add = arr[i] + k

        if subtract < 0:
            continue
        new_min = min(small, subtract)
        new_max = max(big, add)

        result = min(result, new_max-new_min)
    return result

#arr = [3,9,12,16,20]
arr = [1,5,8,10]
k = 2
print(f"Output: {min_height(arr,k)}")
