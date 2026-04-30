def equal_partition(arr):
    n = len(arr)
    total = sum(arr)
    target = total // 2

    # Required subset sizes
    sizes = [n // 2] if n % 2 == 0 else [n // 2, (n + 1) // 2]

    result_subset = None

    def backtrack(index, count, curr_sum, size, path):
        nonlocal result_subset

        if result_subset is not None:
            return

        if count == size:
            if curr_sum == target:
                result_subset = path[:]
            return

        if index == n:
            return

        # Include current element
        path.append(arr[index])
        backtrack(index + 1, count + 1, curr_sum + arr[index], size, path)
        path.pop()

        # Exclude current element
        backtrack(index + 1, count, curr_sum, size, path)

    for size in sizes:
        backtrack(0, 0, 0, size, [])
        if result_subset:
            break

    # Build second subset
    temp = result_subset[:]
    second = []

    for x in arr:
        if x in temp:
            temp.remove(x)
        else:
            second.append(x)

    return [result_subset, second]


# Example 1
arr = [1, 2, 3, 4]
print(equal_partition(arr))
# Example Output: [[1, 4], [2, 3]]

# Example 2
arr = [5, 10, 15]
print(equal_partition(arr))
# Example Output: [[5, 10], [15]]