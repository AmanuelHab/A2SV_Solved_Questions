from collections import Counter
for _ in range(int(input())):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    left_socks = Counter(socks[:l])
    right_socks = Counter(socks[l:])
    
    # Removee matching socks first
    matches = 0

    for color, count in left_socks.items():
        if color in right_socks:
            pair = min(count, right_socks[color])
            matches += pair
            left_socks[color] -= pair
            right_socks[color] -= pair
            
    new_n = n - matches * 2
    new_l = l - matches
    new_r = r - matches

    imbalance = abs(new_l - new_r)
    change_cost = imbalance // 2

    # Balance size
    if new_l > new_r:
        diff = new_l - new_r
        # Give multiple socks
        for sock, count in left_socks.items():
            if count > 1:
                extra = count // 2
                while diff > 0 and extra > 0:
                    left_socks[sock] -= 1
                    right_socks[sock] += 1
                    diff -= 2
                    extra -= 1
            if diff == 0:
                break
            
        # Give unrelated sock
        if diff:
            for sock, count in left_socks.items():
                if diff == 0:
                    break
                if count > 0 and right_socks[sock] == 0:
                    left_socks[sock] -= 1
                    right_socks[sock] += 1
                    diff -= 2
    elif new_r > new_l:
        diff = new_r - new_l
        # Give multiple socks
        for sock, count in right_socks.items():
            if count > 1:
                extra = count // 2
                while diff > 0 and extra > 0:
                    left_socks[sock] += 1
                    right_socks[sock] -= 1
                    diff -= 2
                    extra -= 1
            if diff == 0:
                break

        # Give unrelated sock
        if diff:
            for sock, count in right_socks.items():
                if diff == 0:
                    break
                if count > 0 and left_socks[sock] == 0:
                    left_socks[sock] += 1
                    right_socks[sock] -= 1
                    diff -= 2
                    
    # Remove matches
    new_matches = 0
    for color, count in left_socks.items():
        if color in right_socks:
            pair = min(count, right_socks[color])
            new_matches += pair
            left_socks[color] -= pair
            right_socks[color] -= pair

    newer_n = new_n - 2 * new_matches
    diff_colored = newer_n // 2
    
    print(change_cost + diff_colored)
