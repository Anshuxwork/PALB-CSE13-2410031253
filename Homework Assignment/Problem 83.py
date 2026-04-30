def score_of_parentheses(s):
    stack = [0]

    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            val = stack.pop()

            if val == 0:
                score = 1          # "()"
            else:
                score = 2 * val    # "(A)"

            stack[-1] += score     # add to previous level

    return stack[0]


# Example 1
s = "()()"
print(score_of_parentheses(s))   # Output: 2

# Example 2
s = "(()(()))"
print(score_of_parentheses(s))   # Output: 6

# Example 3
s = "((()))"
print(score_of_parentheses(s))   # Output: 4