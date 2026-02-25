"""Problem 15: Valid Parentheses

Given a string containing brackets, determine if it is valid.
Valid means: opened brackets must be closed by correct type.

Time Complexity: O(n)
Space Complexity: O(n) - for stack storage
"""

def isValid(s):
    """Checks if parentheses string is valid.
    
    Args:
        s: String containing parentheses
    
    Returns:
        True if valid, False otherwise
    """
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map:
            # Closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


if __name__ == "__main__":
    # Test Case 1
    s1 = "()"
    result1 = isValid(s1)
    print(f"Test 1 - String: '{s1}'")
    print(f"Result: Is valid = {result1}")
    print()
    
    # Test Case 2
    s2 = "()[]{}"
    result2 = isValid(s2)
    print(f"Test 2 - String: '{s2}'")
    print(f"Result: Is valid = {result2}")
    print()
    
    # Test Case 3
    s3 = "([)]"
    result3 = isValid(s3)
    print(f"Test 3 - String: '{s3}'")
    print(f"Result: Is valid = {result3}")
