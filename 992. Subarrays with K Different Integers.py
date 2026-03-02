class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysWithAtMostGDistinct(g):
            if g < 1: return 0
            left = count = 0
            n = len(nums)
            freq = defaultdict(int)

            for right in range(n):
                freq[nums[right]] += 1
                while len(freq) > g:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        freq.pop(nums[left])
                    left += 1
                count += right - left + 1
            return count
        return subarraysWithAtMostGDistinct(k) - subarraysWithAtMostGDistinct(k - 1)
