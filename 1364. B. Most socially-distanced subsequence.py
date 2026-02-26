for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    prev = 0
    i = 1
    answer = [nums[0]]
    increasing = True if nums[1] - nums[0] > 0 else False
    while i < n:
        diff = nums[i] - nums[i - 1]
        if (increasing and diff < 0) or (not increasing and diff > 0):
            answer.extend([nums[i - 1]])
            left = i
            prev = 0
            increasing = not increasing
        i += 1
    answer.append(nums[-1])
    print(len(answer))
    print(*answer)
