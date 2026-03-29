class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = set()
        def generate(arr, ind):
            if ind >= len(nums):
                answers.add(tuple(arr))
                return
            generate(arr, ind + 1)
            generate(arr + [nums[ind]], ind + 1)
        generate([], 0)
        return list(answers)