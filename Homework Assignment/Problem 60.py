def combination_sum_k(n, k):
    result = []

    def backtrack(start, remaining, path):
        # If k numbers selected
        if len(path) == k:
            if remaining == 0:
                result.append(path[:])
            return

        # Try numbers from start to 9
        for num in range(start, 10):
            if num > remaining:
                break

            path.append(num)
            backtrack(num + 1, remaining - num, path)
            path.pop()

    backtrack(1, n, [])
    return result


# Example 1
n = 9
k = 3
print(combination_sum_k(n, k))
# Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

# Example 2
n = 3
k = 3
print(combination_sum_k(n, k))
# Output: []