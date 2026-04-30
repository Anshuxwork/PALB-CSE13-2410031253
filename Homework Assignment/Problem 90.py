def largest_string_after_k_deletions(s, k):
    stack = []

    for ch in s:
        # Remove smaller previous characters if possible
        while stack and k > 0 and stack[-1] < ch:
            stack.pop()
            k -= 1

        stack.append(ch)

    # If deletions still remain, remove from end
    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)


# Example 1
s = "ritz"
k = 2
print(largest_string_after_k_deletions(s, k))   # Output: tz

# Example 2
s = "zebra"
k = 3
print(largest_string_after_k_deletions(s, k))   # Output: zr