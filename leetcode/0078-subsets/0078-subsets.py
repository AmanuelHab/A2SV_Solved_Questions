class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSets = []
        def generate(nums, Set):
            if not nums:
                subSets.append(Set)
                return
            generate(nums[1:], Set)
            generate(nums[1:], Set + [nums[0]])
        generate(nums, [])
        return subSets