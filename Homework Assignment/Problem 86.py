def sort_by_length(arr):
    # Python sort is stable, so same-length strings keep original order
    return sorted(arr, key=len)


# Example 1
arr = ["GeeksforGeeeks", "I", "from", "am"]
print(sort_by_length(arr))
# Output: ['I', 'am', 'from', 'GeeksforGeeeks']

# Example 2
arr = ["You", "are", "beautiful", "looking"]
print(sort_by_length(arr))
# Output: ['You', 'are', 'looking', 'beautiful']