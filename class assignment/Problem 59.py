def max_people_visible(arr):
    n = len(arr)
    max_seen = 1

    for i in range(n):
        seen = 1   # include self

        # Look left
        j = i - 1
        while j >= 0:
            if arr[j] < arr[i]:
                seen += 1
                j -= 1
            else:
                break

        # Look right
        j = i + 1
        while j < n:
            if arr[j] < arr[i]:
                seen += 1
                j += 1
            else:
                break

        max_seen = max(max_seen, seen)

    return max_seen


# Example 1
arr = [6, 2, 5, 4, 5, 1, 6]
print(max_people_visible(arr))   # Output: 6

# Example 2
arr = [1, 3, 6, 4]
print(max_people_visible(arr))   # Output: 4