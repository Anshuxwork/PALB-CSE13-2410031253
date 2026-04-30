def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // n][mid % n]
        
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


# Given Examples
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  