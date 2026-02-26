class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        skipped = False
        max_len = length = 0
        left =  0
        for right in range(n):
            # If the window is in valid shrink
            while nums[right] == 0 and skipped:
                length -= 1
                if nums[left] == 0:
                    skipped = False
                left += 1
            length += 1
            if nums[right] == 0:
                skipped = True
            if skipped:
                max_len = max(length - 1, max_len)
            else:
                max_len = max(length, max_len)
        # Decrement if I had already removed a 0
        if skipped:
            return max_len
        return max_len - 1
