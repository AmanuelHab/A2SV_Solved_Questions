class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = set()

        for i in range(n):
            while i + 1 != nums[i]:
                pos = nums[i] - 1
                if nums[i] == nums[pos]:
                    answer.add(nums[i])
                    break
                nums[i], nums[pos] = nums[pos], nums[i]

        return list(answer)