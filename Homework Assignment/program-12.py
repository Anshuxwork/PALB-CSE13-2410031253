"""Problem 12: Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def isPalindrome(s):
    """Checks if string is a valid palindrome.
    
    Args:
        s: String to check
    
    Returns:
        True if palindrome, False otherwise
    """
    # Clean string: keep only alphanumeric and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if it's a palindrome
    return cleaned == cleaned[::-1]


def isPalindrome_twoPointer(s):
    """Two-pointer approach for checking palindrome.
    
    Args:
        s: String to check
    
    Returns:
        True if palindrome, False otherwise
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


if __name__ == "__main__":
    # Test Case 1
    s1 = "A man, a plan, a canal: Panama"
    result1 = isPalindrome(s1)
    print(f"Test 1 - String: '{s1}'")
    print(f"Result: Is palindrome = {result1}")
    print()
    
    # Test Case 2
    s2 = "race a car"
    result2 = isPalindrome(s2)
    print(f"Test 2 - String: '{s2}'")
    print(f"Result: Is palindrome = {result2}")
    print()
    
    # Test Case 3
    s3 = " "
    result3 = isPalindrome(s3)
    print(f"Test 3 - String: '{s3}'")
    print(f"Result: Is palindrome = {result3}")
