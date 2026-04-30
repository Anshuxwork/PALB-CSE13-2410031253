from math import factorial

def count_unique_vowel_strings(s):
    vowels = "aeiou"
    freq = {}

    # Count occurrences of vowels
    for ch in s:
        if ch in vowels:
            freq[ch] = freq.get(ch, 0) + 1

    # Number of distinct vowels present
    distinct = len(freq)

    if distinct == 0:
        return 0

    # Ways to choose one occurrence of each vowel
    choices = 1
    for count in freq.values():
        choices *= count

    # Permutations of selected vowels
    return choices * factorial(distinct)


# Example 1
s = "aeiou"
print(count_unique_vowel_strings(s))   # Output: 120

# Example 2
s = "ae"
print(count_unique_vowel_strings(s))   # Output: 2

# Example 3
s = "aacidf"
print(count_unique_vowel_strings(s))   # Output: 4