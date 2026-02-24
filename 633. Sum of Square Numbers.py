class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(math.sqrt(c))
        l = 0
        r = n
        while l <= r:
            square_sum = l**2 + r **2
            if square_sum == c:
                return True
            elif square_sum < c:
                l += 1
            else:
                r -= 1
        return False
