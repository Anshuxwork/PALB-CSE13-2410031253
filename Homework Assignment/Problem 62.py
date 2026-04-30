def maximize_min_difference(arr, k):
    arr.sort()
    n = len(arr)

    # Check if we can select k elements with minimum gap >= dist
    def can_select(dist):
        count = 1
        last = arr[0]

        for i in range(1, n):
            if arr[i] - last >= dist:
                count += 1
                last = arr[i]

                if count == k:
                    return True
        return False

    low, high = 0, arr[-1] - arr[0]
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if can_select(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


# Example 1
arr = [2, 6, 2, 5]
k = 3
print(maximize_min_difference(arr, k))   # Output: 1

# Example 2
arr = [1, 4, 9, 0, 2, 13, 3]
k = 4
print(maximize_min_difference(arr, k))   # Output: 4