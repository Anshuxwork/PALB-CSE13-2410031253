def previous_greater_elements(arr):
    stack = []
    result = []

    for num in arr:
        # Remove elements smaller than or equal to current
        while stack and stack[-1] <= num:
            stack.pop()

        # Top of stack is previous greater
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        # Push current element
        stack.append(num)

    return result


# Example 1
arr = [10, 4, 2, 20, 40, 12, 30]
print(previous_greater_elements(arr))
# Output: [-1, 10, 4, -1, -1, 40, 40]

# Example 2
arr = [10, 20, 30, 40]
print(previous_greater_elements(arr))
# Output: [-1, -1, -1, -1]