def combinationSum(candidates, target):
    result = []
    
    def dfs(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            dfs(i, current, remaining - candidates[i])
            current.pop()
    
    dfs(0, [], target)
    return result


# Given Examples
print(combinationSum([2,3,6,7], 7))  
print(combinationSum([2,3,5], 8))    
print(combinationSum([2], 1))        