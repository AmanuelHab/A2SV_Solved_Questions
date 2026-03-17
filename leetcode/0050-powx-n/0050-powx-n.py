class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n > 1:
            if n % 2:
                return x * self.myPow(x, n - 1)
            else:
                return self.myPow(x * x, n // 2)
        else:
            if n % 2:
                return  1/x * self.myPow(x, n + 1)
            else:
                return self.myPow(x * x, n // 2)