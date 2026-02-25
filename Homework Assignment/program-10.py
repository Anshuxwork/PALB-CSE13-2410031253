"""Problem 10: Maximum Subarray

Find the contiguous subarray with the largest sum (Kadane's Algorithm).

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxSubArray(nums):
    """Finds the maximum sum of a contiguous subarray.
    
    Args:
        nums: List of integers
    
    Returns:
        The maximum sum of any contiguous subarray
    """
    if not nums:
        return 0
    
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    
    return max_global


if __name__ == "__main__":
    # Test Case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = maxSubArray(nums1)
    print(f"Test 1 - Array: {nums1}")
    print(f"Result: Maximum subarray sum = {result1}")
    print()
    
    # Test Case 2
    nums2 = [5, 4, -1, 7, 8]
    result2 = maxSubArray(nums2)
    print(f"Test 2 - Array: {nums2}")
    print(f"Result: Maximum subarray sum = {result2}")
    print()
    
    # Test Case 3
    nums3 = [-1]
    result3 = maxSubArray(nums3)
    print(f"Test 3 - Array: {nums3}")
    print(f"Result: Maximum subarray sum = {result3}")
