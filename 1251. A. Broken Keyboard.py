from collections import Counter

for _ in range(int(input())):
    chars = list(input())
    n = len(chars)

    res = set()
    i = 0
    while i < n - 1:
        if chars[i] != chars[i + 1]:
            res.add(chars[i])
            i += 1
        else:
            i += 2
    if i == n - 1:
        res.add(chars[-1])
    answer = sorted(list(res))
    
    print("".join(answer))
