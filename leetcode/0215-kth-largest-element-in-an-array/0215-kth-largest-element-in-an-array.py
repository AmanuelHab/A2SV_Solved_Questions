class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = min(nums)
        high = max(nums)

        while low <= high:
            mid = low + (high - low) // 2
            count = 0
            for num in nums:
                if mid <= num:
                    count += 1
                    
            if count >= k:
                low = mid + 1
            else:
                high = mid - 1
        return high