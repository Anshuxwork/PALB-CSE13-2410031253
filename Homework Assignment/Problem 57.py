def count_valid_subarrays(arr):
    n = len(arr)
    stack = []
    count = 0

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Remove elements greater or equal to current
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        # Next smaller element index
        if stack:
            next_smaller = stack[-1]
        else:
            next_smaller = n

        # Number of valid subarrays starting at i
        count += next_smaller - i

        stack.append(i)

    return count


# Example 1
arr = [1, 2, 1]
print(count_valid_subarrays(arr))   # Output: 5

# Example 2
arr = [1, 3, 5, 2]
print(count_valid_subarrays(arr))   # Output: 8