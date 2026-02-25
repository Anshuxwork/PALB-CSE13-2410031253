"""Problem 18: String to Integer (atoi)

Implement myAtoi(string s) which converts a string to a 32-bit signed integer.
Algorithm: discard leading whitespace, check for +/- sign, read digits.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def myAtoi(s):
    """Converts string to integer following atoi rules.
    
    Args:
        s: String to convert
    
    Returns:
        32-bit signed integer
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    # Remove leading whitespace
    s = s.lstrip()
    
    if not s:
        return 0
    
    # Check for sign
    sign = 1
    idx = 0
    if s[0] in ['+', '-']:
        if s[0] == '-':
            sign = -1
        idx = 1
    
    # Read digits
    result = 0
    while idx < len(s) and s[idx].isdigit():
        result = result * 10 + int(s[idx])
        idx += 1
    
    result *= sign
    
    # Clamp to 32-bit integer range
    if result > INT_MAX:
        return INT_MAX
    if result < INT_MIN:
        return INT_MIN
    
    return result


if __name__ == "__main__":
    # Test Case 1
    s1 = "42"
    result1 = myAtoi(s1)
    print(f"Test 1 - String: '{s1}'")
    print(f"Result: {result1}")
    print()
    
    # Test Case 2
    s2 = "   -42"
    result2 = myAtoi(s2)
    print(f"Test 2 - String: '{s2}'")
    print(f"Result: {result2}")
    print()
    
    # Test Case 3
    s3 = "4193 with words"
    result3 = myAtoi(s3)
    print(f"Test 3 - String: '{s3}'")
    print(f"Result: {result3}")
