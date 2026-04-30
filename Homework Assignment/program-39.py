def search_matrix(matrix, target):
    n, m = len(matrix), len(matrix[0])
    left, right = 0, n*m - 1
    
    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // m][mid % m]
        
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False