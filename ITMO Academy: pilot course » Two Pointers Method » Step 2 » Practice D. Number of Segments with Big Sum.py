n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
segments = total = 0
for right in range(n):
    total += nums[right]
    
    # When valid
    while total >= s:
        segments += n - right
        total -= nums[left]
        left += 1

print(segments)
