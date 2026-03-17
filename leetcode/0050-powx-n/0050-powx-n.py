class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = 1
        an = abs(n)
        i = 0
        while an > 0:
            if an % 2 == 0:
                x *= x
                an /= 2
            else:
                answer *= x
                an -= 1
        return answer if n > 0 else 1 / answer