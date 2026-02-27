from collections import defaultdict
 
n, k = map(int, input().split())
nums = list(map(int, input().split()))
 
unique_count = defaultdict(int)
left = segments = 0
 
for right in range(n):
    unique_count[nums[right]] += 1
    # If not valid
    while len(unique_count) > k:
        unique_count[nums[left]] -= 1
        if unique_count[nums[left]] == 0:
            unique_count.pop(nums[left])
        left += 1
 
    # Valid
    segments += right - left + 1
 
print(segments)
