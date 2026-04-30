def count_one_mismatch_pairs(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            diff = 0

            for k in range(len(arr[i])):
                if arr[i][k] != arr[j][k]:
                    diff += 1
                    if diff > 1:
                        break

            if diff == 1:
                count += 1

    return count


# Example 1
arr = ["abc", "abd", "bbd"]
print(count_one_mismatch_pairs(arr))   # Output: 2

# Example 2
arr = ["def", "deg", "dmf", "xef", "dxg"]
print(count_one_mismatch_pairs(arr))   # Output: 4

# Example 3
arr = ["bcde", "bced", "bdce"]
print(count_one_mismatch_pairs(arr))   # Output: 0