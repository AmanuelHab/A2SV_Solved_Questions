class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2:
            curr = x * self.myPow(x, n - 1)
            return curr
            
        curr = self.myPow((x * x) % int(1e9 + 7), n // 2)
        return curr

    def countGoodNumbers(self, n: int) -> int:
        must_be_even = n // 2 + n % 2
        must_be_prime = n // 2
        # exp_num = {
        #     0: 1, 
        #     1: 20
        # }
        
        return (pow(5, n % 2) * self.myPow(20, n // 2)) % int(1e9 + 7)