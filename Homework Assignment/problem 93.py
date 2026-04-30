def shortest_vowel_substring(s1, s2):
    required = set(s1)
    need = len(required)

    freq = {}
    formed = 0
    left = 0
    ans = float('inf')

    for right in range(len(s2)):
        ch = s2[right]

        if ch in required:
            freq[ch] = freq.get(ch, 0) + 1
            if freq[ch] == 1:
                formed += 1

        # Shrink window when all vowels found
        while formed == need:
            ans = min(ans, right - left + 1)

            left_char = s2[left]
            if left_char in required:
                freq[left_char] -= 1
                if freq[left_char] == 0:
                    formed -= 1

            left += 1

    return ans if ans != float('inf') else -1


# Example 1
s1 = "ae"
s2 = "acbaudeq"
print(shortest_vowel_substring(s1, s2))   # Output: 4

# Example 2
s1 = "iou"
s2 = "iuixoiu"
print(shortest_vowel_substring(s1, s2))   # Output: 3

# Example 3
s1 = "aeiou"
s2 = "uoiee"
print(shortest_vowel_substring(s1, s2))   # Output: -1