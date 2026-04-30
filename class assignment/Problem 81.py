def minimum_swaps(s1, s2):
    n = len(s1)

    # Total count of 1s must be even
    if (s1.count('1') + s2.count('1')) % 2 != 0:
        return -1

    type01 = 0   # s1[i]=0, s2[i]=1
    type10 = 0   # s1[i]=1, s2[i]=0

    for i in range(n):
        if s1[i] == '0' and s2[i] == '1':
            type01 += 1
        elif s1[i] == '1' and s2[i] == '0':
            type10 += 1

    # Pairs of same mismatch need 1 swap each
    swaps = type01 // 2 + type10 // 2

    # If one of each remains, need 2 swaps
    if type01 % 2 == 1 and type10 % 2 == 1:
        swaps += 2

    return swaps


# Example 1
s1 = "1100"
s2 = "1111"
print(minimum_swaps(s1, s2))   # Output: 1

# Example 2
s1 = "00011"
s2 = "11001"
print(minimum_swaps(s1, s2))   # Output: -1