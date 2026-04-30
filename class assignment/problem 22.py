def min_length_SubarraySum(arr, x):
    n = len(arr)
    min_length = float('inf')
    current_sum = 0
    start = 0
    for end in range(n):
        current_sum = current_sum + arr[end]

        while current_sum > x:
            min_length = min(min_length, end-start+1)
            current_sum = current_sum - arr[start]
            start = start + 1
    if min_length == float('inf'):
        return 0
    return min_length

arr = [1,4,45,6,0,19]
x = 51
print(f"Output: {min_length_SubarraySum(arr,x)}")
    