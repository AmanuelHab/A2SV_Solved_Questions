class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        freq = defaultdict(int)
        count = 0
        for sm in prefix:
            count += freq[sm - k]
            freq[sm] += 1

        return count