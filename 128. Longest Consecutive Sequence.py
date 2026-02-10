class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        Set = set(nums)  
        num_dist = dict()

        def path_finder(num, num_dist, Set):
            if num in num_dist:
                return num_dist[num]
            if num - 1 in Set: 
                num_dist[num] = path_finder(num - 1, num_dist, Set) + 1
                return num_dist[num]
            else:
                return 1

        for num in nums:
            num_dist[num] = path_finder(num, num_dist, Set)

        max_dist = 0
        for num, dist in num_dist.items():
            max_dist = max(max_dist, dist)
            
        return max_dist
