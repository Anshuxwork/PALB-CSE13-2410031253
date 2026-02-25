"""Problem 17: Reverse String

Reverse a string in-place.

Time Complexity: O(n)
Space Complexity: O(1) if modifying char array in-place
"""

def reverseString_list(s):
    """Reverses string using list (can be modified in-place).
    
    Args:
        s: List of characters
    
    Returns:
        None - modifies list in-place
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverseString_string(s):
    """Reverses a regular string.
    
    Args:
        s: String to reverse
    
    Returns:
        Reversed string
    """
    return s[::-1]


if __name__ == "__main__":
    # Test Case 1 - List reversal
    s1 = ['h', 'e', 'l', 'l', 'o']
    print(f"Test 1 - Before: {s1}")
    reverseString_list(s1)
    print(f"After: {s1}")
    print()
    
    # Test Case 2 - String reversal
    s2 = "hello"
    result2 = reverseString_string(s2)
    print(f"Test 2 - String: '{s2}'")
    print(f"Result: '{result2}'")
    print()
    
    # Test Case 3
    s3 = ['a']
    print(f"Test 3 - Before: {s3}")
    reverseString_list(s3)
    print(f"After: {s3}")
