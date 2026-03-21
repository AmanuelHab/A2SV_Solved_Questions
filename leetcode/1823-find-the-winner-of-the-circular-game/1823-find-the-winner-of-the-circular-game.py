class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [0] * 501
            
        for i in range(1, n+1):
            nums[i] = 1

        def remove(start, remaining):
            if remaining == 1:
                return nums.index(1)
            rmv = start % 501
            i = k 
            while i > 0:
                rmv = (rmv + 1) % 501
                if nums[rmv] == 1:
                    i -= 1
            nums[rmv]  = 0
            remaining -= 1  
            
            return remove(rmv, remaining)
            
        return remove(0, n)