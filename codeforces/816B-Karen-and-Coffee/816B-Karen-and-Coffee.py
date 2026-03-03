n, k, q = map(int, input().split())
count = [0] * 200002
for _ in range(n):
    l, r = map(int, input().split())
    count[l] += 1
    count[r + 1] -= 1
for i in range(1, len(count)):
    count[i] += count[i - 1]

for i in range(1, len(count)):
    if count[i] >= k:
        count[i] = 1
    else:
        count[i] = 0
        
for i in range(1, len(count)):
    count[i] += count[i - 1]


for i in range(q):
    a, b = map(int, input().split())
    cnt = count[b] - count[a - 1]
    print(cnt)