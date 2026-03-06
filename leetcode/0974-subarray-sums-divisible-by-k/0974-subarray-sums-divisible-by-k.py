class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_count = {0: 1}
        prefix_sum = count = 0
        for num in nums:
            prefix_sum += num
            # Check a complement
            complement = (k - (prefix_sum % k)) % k
            if complement in sum_count:
                count += sum_count[complement]
            sum_count[complement] = sum_count.get(complement, 0) + 1
            
        return count