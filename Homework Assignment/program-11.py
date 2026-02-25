"""Problem 11: Contains Duplicate

Given an array, determine if it contains duplicate elements.

Time Complexity: O(n)
Space Complexity: O(n) - using set
"""

def containsDuplicate(nums):
    """Checks if array contains duplicate elements.
    
    Args:
        nums: List of integers
    
    Returns:
        True if duplicates exist, False otherwise
    """
    return len(nums) != len(set(nums))


def containsDuplicate_optimized(nums):
    """Optimized version that returns early.
    
    Args:
        nums: List of integers
    
    Returns:
        True if duplicates exist, False otherwise
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 1]
    result1 = containsDuplicate(nums1)
    print(f"Test 1 - Array: {nums1}")
    print(f"Result: Contains duplicate = {result1}")
    print()
    
    # Test Case 2
    nums2 = [1, 2, 3, 4]
    result2 = containsDuplicate(nums2)
    print(f"Test 2 - Array: {nums2}")
    print(f"Result: Contains duplicate = {result2}")
    print()
    
    # Test Case 3
    nums3 = [99, 99]
    result3 = containsDuplicate(nums3)
    print(f"Test 3 - Array: {nums3}")
    print(f"Result: Contains duplicate = {result3}")
