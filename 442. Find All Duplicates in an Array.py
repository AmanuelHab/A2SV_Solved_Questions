class Solution(object):
    def findDuplicates(self, nums):
        n = len(nums)
        answer = []
        for i in range(n):
            val = abs(nums[i])
            index = val - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                answer.append(val)
        return answer
