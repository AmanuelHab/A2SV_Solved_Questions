class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0
        maxi = nums[-1]

        for i in range(n - 2, -1, -1):
            divisions = math.ceil(nums[i] / maxi)
            op += divisions - 1

            mini = nums[i] // divisions 
            maxi = mini
        return op