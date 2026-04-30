def find132pattern(arr):
    n = len(arr)
    if n < 3:
        return False

    stack = []
    third = float('-inf')   # candidate for arr[k]

    # Traverse from right to left
    for i in range(n - 1, -1, -1):

        # If current element is smaller than arr[k]
        if arr[i] < third:
            return True

        # Update arr[k]
        while stack and arr[i] > stack[-1]:
            third = stack.pop()

        # Push current as possible arr[j]
        stack.append(arr[i])

    return False


# Example 1
arr = [4, 7, 11, 5, 13, 2]
print(find132pattern(arr))   # True

# Example 2
arr = [11, 11, 12, 9]
print(find132pattern(arr))   # False