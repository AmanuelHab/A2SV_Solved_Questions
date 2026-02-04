class Solution(object):
    def missingNumber(self, nums):
        num_c = dict()
        for num in nums:
            num_c[num] = num
        index = 0
        while index < len(nums):
            if index not in num_c:
                return index
            index += 1
        return index
