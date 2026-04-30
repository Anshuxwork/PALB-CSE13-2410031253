from collections import Counter

def check_permutation_substring(txt, pat):
    n = len(txt)
    m = len(pat)

    if m > n:
        return False

    pat_count = Counter(pat)
    window_count = Counter(txt[:m])

    # Check first window
    if window_count == pat_count:
        return True

    # Sliding window
    for i in range(m, n):
        add_char = txt[i]
        remove_char = txt[i - m]

        window_count[add_char] += 1
        window_count[remove_char] -= 1

        if window_count[remove_char] == 0:
            del window_count[remove_char]

        if window_count == pat_count:
            return True

    return False


# Example 1
txt = "geeks"
pat = "eke"
print(check_permutation_substring(txt, pat))   # Output: True

# Example 2
txt = "programming"
pat = "rain"
print(check_permutation_substring(txt, pat))   # Output: False