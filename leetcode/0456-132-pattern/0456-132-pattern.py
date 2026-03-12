class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # Store the previous minimum for each numbers 
        prev_min = defaultdict(lambda: -1)
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                prev_min[i] = stack[0] 
            stack.append(i)
 
        # Store the previous maximum for each numbers
        prev_max = defaultdict(lambda: -1)
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                prev_max[i] = stack[-1]
            stack.append(i)
            
        for k in range(n):
            j = prev_max[k]
            i = prev_min[j]
            if i == -1 or j == -1:
                continue
            if i < j < k and nums[i] < nums[k] < nums[j]:
                return True
        return False