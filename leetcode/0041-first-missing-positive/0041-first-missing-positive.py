class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while i + 1 != nums[i]:
                pos = nums[i] - 1
                if pos < 0 or pos >= n or nums[i] == nums[pos]:
                    break
                nums[i], nums[pos] = nums[pos], nums[i]
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1