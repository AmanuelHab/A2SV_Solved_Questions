from bisect import bisect_left, bisect_right
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(sorted(map(int, input().split())))

    # print(a)
    if a[0] > b[0] - a[0]:
        a[0] = b[0] - a[0]
    for i in range(1, n):
        # Minimize the number
        find = a[i-1] + a[i]
        ind = bisect_left(b, find)
        if ind == len(b):
            continue
        mini = b[ind] - a[i]

        if a[i] >= a[i-1] and mini >= a[i-1]:
            a[i] = min(a[i], mini)
        elif mini >= a[i]:
            a[i] = mini
        else:
            break

    if a == sorted(a):
        print("YES")
    else:
        print("NO")