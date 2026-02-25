"""Problem 14: Group Anagrams

Given an array of strings, group the anagrams together.

Time Complexity: O(n * k log k) where n is number of strings, k is max length
Space Complexity: O(n * k)
"""

def groupAnagrams(strs):
    """Groups anagrams from list of strings.
    
    Args:
        strs: List of strings
    
    Returns:
        List of lists, each containing anagrams
    """
    anagram_map = {}
    
    for word in strs:
        # Sort characters to use as key
        sorted_word = ''.join(sorted(word))
        
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []
        anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())


if __name__ == "__main__":
    # Test Case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = groupAnagrams(strs1)
    print(f"Test 1 - Strings: {strs1}")
    print(f"Result: {result1}")
    print()
    
    # Test Case 2
    strs2 = [""]
    result2 = groupAnagrams(strs2)
    print(f"Test 2 - Strings: {strs2}")
    print(f"Result: {result2}")
    print()
    
    # Test Case 3
    strs3 = ["a"]
    result3 = groupAnagrams(strs3)
    print(f"Test 3 - Strings: {strs3}")
    print(f"Result: {result3}")
