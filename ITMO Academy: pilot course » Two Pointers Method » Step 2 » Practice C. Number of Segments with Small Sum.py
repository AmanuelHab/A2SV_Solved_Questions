n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
segments = total = 0
for right in range(n):
    total += nums[right]
    # If invalid
    while total > s:
        total -= nums[left]
        left += 1
    distance = right - left + 1

    segments += distance
    # print(nums[left: right + 1], total)
    # print(nums[right], distance, segments)

print(segments)
