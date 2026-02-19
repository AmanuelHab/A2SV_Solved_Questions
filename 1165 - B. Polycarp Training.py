n = int(input())
nums = list(map(int, input().split()))
nums.sort()
i = 1

for j in range(n):
    if nums[j] >= i:
        i += 1
        
print(i - 1)
