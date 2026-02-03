class Solution(object):
    def isPalindrome(self, x):
        x_string = str(x)
        n = len(x_string)
        for i in range(n // 2):
            if x_string[i] != x_string[n - i - 1]:
                return False
        else:
            return True
