def min_add_to_make_valid(s):
    open_count = 0
    additions = 0

    for ch in s:
        if ch == '(':
            open_count += 1
        else:  # ')'
            if open_count > 0:
                open_count -= 1
            else:
                additions += 1

    # unmatched '(' also need closing brackets
    return additions + open_count


# Example 1
s = "(()("
print(min_add_to_make_valid(s))   # Output: 2

# Example 2
s = ")))"
print(min_add_to_make_valid(s))   # Output: 3

# Example 3
s = ")()()"
print(min_add_to_make_valid(s))   # Output: 1