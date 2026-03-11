class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0
        queue = deque(nums[:3])
        if queue[0] == 0:
            for i in range(3):
                queue[i] ^= 1
            op += 1
            
        for i in range(3, n):
            queue.append(nums[i])
            queue.popleft()

            if queue[0] == 0:
                for i in range(3):
                    queue[i] ^= 1
                op += 1
        if 0 in queue:
            return -1
        return op