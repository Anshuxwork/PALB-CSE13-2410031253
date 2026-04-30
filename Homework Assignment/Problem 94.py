def countBalanced(arr):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    prefix = 0
    freq = {0: 1}   # prefix sum frequency
    ans = 0

    for s in arr:
        v = 0
        c = 0

        for ch in s:
            if ch in vowels:
                v += 1
            else:
                c += 1

        diff = v - c
        prefix += diff

        ans += freq.get(prefix, 0)
        freq[prefix] = freq.get(prefix, 0) + 1

    return ans
arr = ["aeio", "aa", "bc", "ot", "cdbd"]
print(countBalanced(arr))

arr = ["ab", "be"]
print(countBalanced(arr))

arr = ["tz", "gfg", "ae"]
print(countBalanced(arr))

