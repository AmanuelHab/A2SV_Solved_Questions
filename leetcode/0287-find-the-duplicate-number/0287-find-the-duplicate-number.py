class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i + 1 != nums[i]:
                pos = nums[i] - 1
                if nums[pos] == nums[i]:
                    return nums[i]
                nums[i], nums[pos] = nums[pos], nums[i]