from bisect import bisect_right

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    for z in range(2, n):
        for y in range(1, z):
            x = max(2 * arr[z], arr[-1]) - arr[y] - arr[z]
            xs = y - bisect_right(arr, x)
            # print(f"arr[x]= {x}, y={y}, z={z}, xs={xs}, answer={answer}")
            if xs > 0:
                answer += xs
    print(answer)