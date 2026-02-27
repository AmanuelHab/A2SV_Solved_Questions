from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 0
count = defaultdict(int)
max_len = 0
l, r = 1, n

for right in range(n):
    count[a[right]] += 1
    # if not valid
    while len(count.keys()) > k:
        count[a[left]] -= 1
        if count[a[left]] == 0:
            count.pop(a[left])
        left += 1
    if right - left + 1 > max_len:
        max_len = right - left + 1
        l = left + 1
        r = right + 1
print(l, r)
