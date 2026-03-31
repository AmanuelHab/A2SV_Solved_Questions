class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answers = set()
        def generate(arr, ind):
            if len(arr) > 1:
                answers.add(tuple(arr))
            if ind >= len(nums):
                return
            
            generate(arr, ind + 1)
            if arr:
                if arr[-1] <= nums[ind]:
                    generate(arr + [nums[ind]], ind + 1)
            else:
                generate(arr + [nums[ind]], ind + 1)
        generate([], 0)

        return list(answers)