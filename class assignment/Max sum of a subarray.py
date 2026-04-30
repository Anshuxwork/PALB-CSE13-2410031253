def maxSumSubArray(a):
    current_sum = a[0]
    max_sumArray = a[0]
    for i in range (1,len(a)):
        current_sum = max(a[i], a[i]+current_sum)
        max_sumArray = max(max_sumArray, current_sum)
    return max_sumArray

arr = [2,3,-8,7,-1,2,3]
print(f"Output: {maxSumSubArray(arr)}")