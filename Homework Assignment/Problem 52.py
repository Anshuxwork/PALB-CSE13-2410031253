def footpath_cost(n, m, a, queries):
    INF = float('inf')

    # 4 prefix/suffix minimum matrices
    tl = [[INF] * m for _ in range(n)]  # top-left
    tr = [[INF] * m for _ in range(n)]  # top-right
    bl = [[INF] * m for _ in range(n)]  # bottom-left
    br = [[INF] * m for _ in range(n)]  # bottom-right

    # Top-Left minimum
    for i in range(n):
        for j in range(m):
            tl[i][j] = a[i][j]
            if i > 0:
                tl[i][j] = min(tl[i][j], tl[i - 1][j])
            if j > 0:
                tl[i][j] = min(tl[i][j], tl[i][j - 1])

    # Top-Right minimum
    for i in range(n):
        for j in range(m - 1, -1, -1):
            tr[i][j] = a[i][j]
            if i > 0:
                tr[i][j] = min(tr[i][j], tr[i - 1][j])
            if j < m - 1:
                tr[i][j] = min(tr[i][j], tr[i][j + 1])

    # Bottom-Left minimum
    for i in range(n - 1, -1, -1):
        for j in range(m):
            bl[i][j] = a[i][j]
            if i < n - 1:
                bl[i][j] = min(bl[i][j], bl[i + 1][j])
            if j > 0:
                bl[i][j] = min(bl[i][j], bl[i][j - 1])

    # Bottom-Right minimum
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            br[i][j] = a[i][j]
            if i < n - 1:
                br[i][j] = min(br[i][j], br[i + 1][j])
            if j < m - 1:
                br[i][j] = min(br[i][j], br[i][j + 1])

    ans = []

    for R, C in queries:
        r = R - 1   # convert to 0-based
        c = C - 1

        total = 0

        # Top-left section
        if r - 1 >= 0 and c - 1 >= 0:
            total += tl[r - 1][c - 1]

        # Top-right section
        if r - 1 >= 0 and c + 1 < m:
            total += tr[r - 1][c + 1]

        # Bottom-left section
        if r + 1 < n and c - 1 >= 0:
            total += bl[r + 1][c - 1]

        # Bottom-right section
        if r + 1 < n and c + 1 < m:
            total += br[r + 1][c + 1]

        ans.append(total)

    return ans


# Example 1
n = 3
m = 3
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
queries = [[2, 2]]

print(*footpath_cost(n, m, a, queries))   # 20


# Example 2
n = 3
m = 4
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4]
]
queries = [[3, 4]]

print(*footpath_cost(n, m, a, queries))   # 1