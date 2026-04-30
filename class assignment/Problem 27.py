def spiral_traversal(mat):
    result = []
    
    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    
    return result


# Example 1
mat1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
print("Output:", spiral_traversal(mat1))

# Example 2
mat2 = [[1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]]
print("Output:", spiral_traversal(mat2))

# Example 3
mat3 = [[32, 44, 27, 23],
        [54, 28, 50, 62]]
print("Output:", spiral_traversal(mat3))