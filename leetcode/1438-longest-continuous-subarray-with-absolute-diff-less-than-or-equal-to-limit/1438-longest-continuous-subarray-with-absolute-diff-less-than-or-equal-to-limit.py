class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        decr_queue = deque()
        incr_queue = deque()
        left = max_len = 0
        for right in range(n):
            #Add element to increasing queue
            while incr_queue and nums[incr_queue[-1]] > nums[right]:
                incr_queue.pop()
            incr_queue.append(right)
            
            #Add element to decreasing queue
            while decr_queue and nums[decr_queue[-1]] < nums[right]:
                decr_queue.pop()
            decr_queue.append(right)

            # If not valid 
            while incr_queue and decr_queue and abs(nums[incr_queue[0]] - nums[decr_queue[0]]) > limit:
                if incr_queue[0] == left:
                    incr_queue.popleft()
                if decr_queue[0] == left:
                    decr_queue.popleft()
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len