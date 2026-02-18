class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Store nums and their indices
        num_ind = defaultdict(list)
        for i in range(n):
            num_ind[nums[i]].append(i)

        sorted_count = dict(sorted(num_ind.items()))

        # Store nums with the number of previous count
        num_prev = defaultdict(list)
        prev_count = 0
        for num, indices in sorted_count.items():
            num_prev[num] = prev_count
            prev_count += len(indices)
        
        answer = [None] * n

        for i in range(n):
            answer[i] = num_prev[nums[i]]

        return answer
