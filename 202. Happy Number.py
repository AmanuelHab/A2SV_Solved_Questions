class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            sn = str(n)
            sum_sq = 0
            for ch in sn: 
                sum_sq += pow(int(ch), 2)
            if sum_sq == 1:
                return True
            else:
                if sum_sq in seen:
                    return False
                else: 
                    seen.add(sum_sq)
                n = sum_sq
