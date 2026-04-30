import heapq

def min_operations(arr):
    # Max heap using negative values
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)

    total_sum = sum(arr)
    target = total_sum / 2

    current_sum = total_sum
    operations = 0

    while current_sum > target:
        # Get largest element
        largest = -heapq.heappop(max_heap)

        # Halve it
        half = largest / 2

        # Reduce current sum
        current_sum -= half

        # Push halved value back
        heapq.heappush(max_heap, -half)

        operations += 1

    return operations


# Example 1
arr = [8, 6, 2]
print(min_operations(arr))   # Output: 3

# Example 2
arr = [9, 1, 2]
print(min_operations(arr))   # Output: 2