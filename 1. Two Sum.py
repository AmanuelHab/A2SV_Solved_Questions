class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_ind = dict()

        for i in range(len(nums)):
            if nums[i] in diff_ind:
                return [i, diff_ind[nums[i]]]
            diff = target - nums[i]
            diff_ind[diff] = i
