class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # Count frequency and find dominant number
        dominant = -1
        right_freq = defaultdict(int)
        for num in nums:
            right_freq[num] += 1
            if right_freq[num] > n / 2:
                dominant = num
        
        #Iterate through nums editting the frequencies
        left_freq = defaultdict(int)

        for i in range(n):
            left_freq[nums[i]] += 1
            right_freq[nums[i]] -= 1

            if left_freq[dominant] > (i + 1) / 2 and right_freq[dominant] > (n - i - 1) / 2:
                return i
        return -1
