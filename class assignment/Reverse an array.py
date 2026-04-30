class Solution:
    def reverseArray(self,arr):
        left , right =0, len(arr)-1
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left = left + 1
            right = right - 1
        return arr
        
        




obj = Solution()
arr = [1,4,5,6,7,9]
print("Array: ",arr)

result = obj.reverseArray(arr)
print("Reverse Array: ", result)
