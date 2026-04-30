def previous_smaller_elements(arr):
    stack = []
    result = []

    for num in arr:
        # Remove elements greater than or equal to current
        while stack and stack[-1] >= num:
            stack.pop()

        # Top of stack is previous smaller
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        # Push current element
        stack.append(num)

    return result


# Example 1
arr = [1, 6, 2]
print(previous_smaller_elements(arr))   # [-1, 1, 1]

# Example 2
arr = [1, 5, 0, 3, 4, 5]
print(previous_smaller_elements(arr))   # [-1, 1, -1, 0, 3, 4]