class Solution:
    def reverseArray(self,array):
        #return array[::-1]
        #left = 0
        #right = len(arr)-1
        left ,right = 0 , len(array)-1
        while left < right:
            array[left],array[right] = array[right],array[left]
            left = left + 1 
            right = right - 1 

obj = Solution()
array = [1,2,3,4,5,6,7,8,9]

result = obj.reverseArray(array)