def union_arrays(a, b):
    union_set = set(a) | set(b)
    return list(union_set)

# Example
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(union_arrays(a, b))