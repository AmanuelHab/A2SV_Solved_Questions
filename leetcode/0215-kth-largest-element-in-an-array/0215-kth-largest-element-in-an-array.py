class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        offset = min(nums)
        freq = [0] * (max(nums) - offset + 1)

        for num in nums:
            freq[num - offset] += 1

        for i in range(len(freq)-1, -1, -1):
            f = freq[i]
            num = i + offset
            k -= f
            if k <= 0:
                return num