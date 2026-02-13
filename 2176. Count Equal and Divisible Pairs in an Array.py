class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num_ind = defaultdict(list)

        # Filter
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    num_ind[nums[i]].append(i)
                    num_ind[nums[j]].append(j)

        # Count
        pairs = 0
        for indices in num_ind.values():
            pairs += len(indices) // 2
        return pairs
