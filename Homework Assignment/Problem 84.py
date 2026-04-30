def min_time_difference(arr):
    # Convert HH:MM:SS to total seconds
    times = []

    for t in arr:
        h, m, s = map(int, t.split(":"))
        total = h * 3600 + m * 60 + s
        times.append(total)

    # Sort times
    times.sort()

    min_diff = float('inf')

    # Adjacent differences
    for i in range(1, len(times)):
        min_diff = min(min_diff, times[i] - times[i - 1])

    # Circular difference (last to first across midnight)
    day_seconds = 24 * 3600
    wrap_diff = day_seconds - times[-1] + times[0]

    min_diff = min(min_diff, wrap_diff)

    return min_diff


# Example 1
arr = ["12:30:15", "12:30:45"]
print(min_time_difference(arr))   # Output: 30

# Example 2
arr = ["00:00:01", "23:59:59", "00:00:05"]
print(min_time_difference(arr))   # Output: 2