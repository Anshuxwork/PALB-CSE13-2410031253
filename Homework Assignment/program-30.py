import bisect

def matrix_median(mat):
    n = len(mat)
    m = len(mat[0])
    
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)
    
    while low < high:
        mid = (low + high) // 2
        count = 0
        
        for row in mat:
            count += bisect.bisect_right(row, mid)
        
        if count <= (n * m) // 2:
            low = mid + 1
        else:
            high = mid
    
    return low