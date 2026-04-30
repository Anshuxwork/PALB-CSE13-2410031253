def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    result = []
    
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        
        if arr1[i] == arr2[j] == arr3[k]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    
    return result if result else [-1]