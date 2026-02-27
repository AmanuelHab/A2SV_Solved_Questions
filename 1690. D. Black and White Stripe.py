for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    
    count = 0
    min_paint = n

    left = max_len = 0

    for right in range(n):
        if s[right] == 'W':
            count += 1
        while right - left + 1 > k:
            if s[left] == 'W':
                count -= 1
            left += 1
        
        if right - left + 1 == k:
            min_paint = min(min_paint, count)
    print(min_paint)
