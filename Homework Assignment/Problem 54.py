def min_people_required(arr):
    n = len(arr)
    intervals = []

    # Build valid intervals
    for i in range(n):
        if arr[i] != -1:
            left = max(0, i - arr[i])
            right = min(n - 1, i + arr[i])
            intervals.append((left, right))

    # Sort by start time
    intervals.sort()

    count = 0
    i = 0
    covered_end = -1

    while covered_end < n - 1:
        farthest = covered_end

        # Find all intervals starting before next uncovered point
        while i < len(intervals) and intervals[i][0] <= covered_end + 1:
            farthest = max(farthest, intervals[i][1])
            i += 1

        # No progress means impossible
        if farthest == covered_end:
            return -1

        count += 1
        covered_end = farthest

    return count


# Example 1
arr = [1, 2, 1, 0]
print(min_people_required(arr))   # Output: 1

# Example 2
arr = [2, 3, 4, -1, 2, 0, 0, -1, 0]
print(min_people_required(arr))   # Output: -1

# Example 3
arr = [0, 1, 0, -1]
print(min_people_required(arr))   # Output: -1