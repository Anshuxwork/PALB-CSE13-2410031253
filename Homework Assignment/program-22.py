"""Problem 22: Trapping Rain Water

Given elevation map, calculate how much rain water can be trapped.

Time Complexity: O(n)
Space Complexity: O(1) for two-pointer approach
"""

def trap(height):
    """Calculates water trapped between elevation bars.
    
    Args:
        height: List of integers representing elevation
    
    Returns:
        Total units of water trapped
    """
    if not height or len(height) < 3:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


if __name__ == "__main__":
    # Test Case 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result1 = trap(height1)
    print(f"Test 1 - Height map: {height1}")
    print(f"Result: Water trapped = {result1} units")
    print()
    
    # Test Case 2
    height2 = [4, 2, 0, 3, 2, 5]
    result2 = trap(height2)
    print(f"Test 2 - Height map: {height2}")
    print(f"Result: Water trapped = {result2} units")
    print()
    
    # Test Case 3
    height3 = []
    result3 = trap(height3)
    print(f"Test 3 - Height map: {height3}")
    print(f"Result: Water trapped = {result3} units")
