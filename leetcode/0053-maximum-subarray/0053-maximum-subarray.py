class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        prefix = nums[0]
        for i in range(1, n):
            prefix +=  nums[i]
            
            prefix = max(nums[i], prefix)
            max_sum = max(prefix, max_sum)
        return max_sum