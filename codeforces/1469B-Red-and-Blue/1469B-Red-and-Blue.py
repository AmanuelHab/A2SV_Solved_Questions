for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    for i in range(1, n):
        r[i] += r[i - 1]
    for i in range(1, m):
        b[i] += b[i - 1]

    result = max(max(r), 0) + max(max(b), 0)
    print(result)