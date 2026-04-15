class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        lost = 0
        for i in range(len(nums)):
            while i + 1 != nums[i]:
                target_ind = nums[i] -1
                if nums[target_ind] == nums[i]:
                    dup = nums[i]
                    break
                nums[i], nums[target_ind] = nums[target_ind], nums[i]
                
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                lost = i + 1
                break
        return [dup, lost]