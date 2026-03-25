class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def generate(nums, curr):
            if not nums:
                permutations.append(curr)
                return
            for num in nums:
                new_num = nums[:]
                new_num.remove(num)
                
                generate(new_num, curr + [num])
        generate(nums, [])
        return permutations