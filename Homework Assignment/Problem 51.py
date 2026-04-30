def build_prefix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    prefix = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            prefix[i][j] = matrix[i][j]

            if i > 0:
                prefix[i][j] += prefix[i - 1][j]

            if j > 0:
                prefix[i][j] += prefix[i][j - 1]

            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i - 1][j - 1]

    return prefix


def query_sum(prefix, r1, c1, r2, c2):
    result = prefix[r2][c2]

    if r1 > 0:
        result -= prefix[r1 - 1][c2]

    if c1 > 0:
        result -= prefix[r2][c1 - 1]

    if r1 > 0 and c1 > 0:
        result += prefix[r1 - 1][c1 - 1]

    return result


# Input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

queries = [
    [0, 0, 2, 2],
    [1, 0, 2, 1]
]

# Build prefix sum matrix
prefix = build_prefix(matrix)

# Process queries
for q in queries:
    r1, c1, r2, c2 = q
    print(query_sum(prefix, r1, c1, r2, c2))