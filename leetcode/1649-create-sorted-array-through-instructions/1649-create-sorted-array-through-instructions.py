class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = len(instructions)
        nums = []
        cost = 0
        for instr in instructions:
            left = bisect_left(nums, instr)
            right = len(nums) - bisect_right(nums, instr)
            cost += min(left, right)
            nums.insert(left, instr)
            
        return cost % (10**9 + 7)