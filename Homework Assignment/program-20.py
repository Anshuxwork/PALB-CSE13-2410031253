"""Problem 20: Median of Two Sorted Arrays

Given two sorted arrays, find the median of the two sorted arrays.

Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
"""

def findMedianSortedArrays(nums1, nums2):
    """Finds median of two sorted arrays.
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
    
    Returns:
        Median of combined arrays
    """
    # Ensure nums1 is smaller array for binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = (m + n + 1) // 2 - cut1
        
        # Handle boundary cases
        left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
        left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
        right1 = float('inf') if cut1 == m else nums1[cut1]
        right2 = float('inf') if cut2 == n else nums2[cut2]
        
        if left1 <= right2 and left2 <= right1:
            # Check if total length is odd or even
            if (m + n) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return max(left1, left2)
        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    
    return -1


if __name__ == "__main__":
    # Test Case 1
    nums1_1 = [1, 3]
    nums2_1 = [2]
    result1 = findMedianSortedArrays(nums1_1, nums2_1)
    print(f"Test 1 - Array 1: {nums1_1}, Array 2: {nums2_1}")
    print(f"Result: Median = {result1}")
    print()
    
    # Test Case 2
    nums1_2 = [1, 2]
    nums2_2 = [3, 4]
    result2 = findMedianSortedArrays(nums1_2, nums2_2)
    print(f"Test 2 - Array 1: {nums1_2}, Array 2: {nums2_2}")
    print(f"Result: Median = {result2}")
    print()
    
    # Test Case 3
    nums1_3 = [0, 0]
    nums2_3 = [0, 0]
    result3 = findMedianSortedArrays(nums1_3, nums2_3)
    print(f"Test 3 - Array 1: {nums1_3}, Array 2: {nums2_3}")
    print(f"Result: Median = {result3}")
