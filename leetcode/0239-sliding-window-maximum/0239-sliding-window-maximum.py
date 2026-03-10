class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        answer = []

        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        answer.append(nums[queue[0]])
        
        for i in range(k, n):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            answer.append(nums[queue[0]])

        return answer