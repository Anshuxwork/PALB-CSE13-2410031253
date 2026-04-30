from collections import Counter

def sort_by_frequency(s):
    freq = Counter(s)

    # Sort by (frequency, character)
    chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))

    result = ""

    for ch, count in chars:
        result += ch * count

    return result


# Example 1
s = "geeksforgeeks"
print(sort_by_frequency(s))   # Output: forggkksseee

# Example 2
s = "abc"
print(sort_by_frequency(s))   # Output: abc