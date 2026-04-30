def count_less_equal(arr, x):
    count = 0

    for num in arr:
        if num <= x:
            count += 1

    return count


# Example 1
arr = [4, 5, 8, 1, 3]
x = 6
print(count_less_equal(arr, x))   # Output: 4

# Example 2
arr = [6, 10, 12, 15, 2, 4, 5]
x = 14
print(count_less_equal(arr, x))   # Output: 6