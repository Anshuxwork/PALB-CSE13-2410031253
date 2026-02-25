"""Problem 13: Valid Anagram

Given two strings, determine if they are anagrams of each other.
An anagram is a word formed by rearranging letters of another word.

Time Complexity: O(n log n) for sorting approach
Space Complexity: O(1) or O(n) depending on approach
"""

def isAnagram_sorting(s, t):
    """Checks if strings are anagrams using sorting.
    
    Args:
        s: First string
        t: Second string
    
    Returns:
        True if anagrams, False otherwise
    """
    return sorted(s) == sorted(t)


def isAnagram_counting(s, t):
    """Checks if strings are anagrams using character count.
    
    Args:
        s: First string
        t: Second string
    
    Returns:
        True if anagrams, False otherwise
    """
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    # Count characters in first string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrease count for characters in second string
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True


if __name__ == "__main__":
    # Test Case 1
    s1, t1 = "anagram", "nagaram"
    result1 = isAnagram_sorting(s1, t1)
    print(f"Test 1 - String 1: '{s1}', String 2: '{t1}'")
    print(f"Result: Are anagrams = {result1}")
    print()
    
    # Test Case 2
    s2, t2 = "rat", "car"
    result2 = isAnagram_sorting(s2, t2)
    print(f"Test 2 - String 1: '{s2}', String 2: '{t2}'")
    print(f"Result: Are anagrams = {result2}")
    print()
    
    # Test Case 3
    s3, t3 = "a", "b"
    result3 = isAnagram_counting(s3, t3)
    print(f"Test 3 - String 1: '{s3}', String 2: '{t3}'")
    print(f"Result: Are anagrams = {result3}")
