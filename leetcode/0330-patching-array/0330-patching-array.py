class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        length = len(nums)

        add = 0
        obtainable = 0
        i = 0
        while i < length and obtainable < n:
            curr = nums[i]
            unobtainable = obtainable + 1
            
            # Add necessary numbers that we don't have
            if curr > unobtainable:
                add += 1
                obtainable += unobtainable
            # Add numbers that we have
            else:
                obtainable += curr
                i += 1

        # If the target is not reached after using all nums
        while obtainable < n:
            unobtainable = obtainable + 1
            obtainable += unobtainable
            add += 1
        
        return add