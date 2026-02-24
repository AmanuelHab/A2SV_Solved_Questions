from collections import Counter

for _ in range(int(input())):
    needle = input()
    hay = input()
    s_len = len(needle)
    t_len = len(hay)
    n_counter = Counter(needle)
    h_counter = Counter(hay)

    for ch, count in n_counter.items():
        if h_counter[ch] < count:
            print("Impossible")
            break
    else:
        hay = []
        for ch, count in (h_counter - n_counter).items():
            hay.extend([ch] * count)
        hay.sort()

        h_len = len(hay)   

        answer = []
        i = j = 0
        while i < s_len and j < h_len:
            if needle[i] <= hay[j]:
                answer.append(needle[i])
                i += 1
            else:
                answer.append(hay[j])
                j += 1
        answer.extend(needle[i:])
        answer.extend(hay[j:])

        print("".join(answer))
