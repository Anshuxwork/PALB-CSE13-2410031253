"""Problem 19: Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating chars.

Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is charset size
"""

def lengthOfLongestSubstring(s):
    """Finds length of longest substring without repeating characters.
    
    Args:
        s: Input string
    
    Returns:
        Length of longest substring
    """
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If character seen before and within current window
        if char in char_index and char_index[char] >= start:
            # Move start to skip duplicate
            start = char_index[char] + 1
        
        # Update character's last seen index
        char_index[char] = end
        
        # Update max length
        max_length = max(max_length, end - start + 1)
    
    return max_length


if __name__ == "__main__":
    # Test Case 1
    s1 = "abcabcbb"
    result1 = lengthOfLongestSubstring(s1)
    print(f"Test 1 - String: '{s1}'")
    print(f"Result: Length = {result1}")
    print()
    
    # Test Case 2
    s2 = "bbbbb"
    result2 = lengthOfLongestSubstring(s2)
    print(f"Test 2 - String: '{s2}'")
    print(f"Result: Length = {result2}")
    print()
    
    # Test Case 3
    s3 = "pwwkew"
    result3 = lengthOfLongestSubstring(s3)
    print(f"Test 3 - String: '{s3}'")
    print(f"Result: Length = {result3}")
