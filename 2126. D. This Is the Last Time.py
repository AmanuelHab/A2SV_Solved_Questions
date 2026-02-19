for _ in range(int(input())):
    n, k = map(int, input().split())
    casinos = [list(map(int, input().split())) for _ in range(n)]

    casinos.sort(key=lambda x : (x[0], -x[2]))

    i = 0
    while i < n:
        l, r, real = casinos[i]
        
        if l <= k and k < real:
            k = real
          
        i += 1
    print(k)
