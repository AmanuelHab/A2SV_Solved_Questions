class Solution:
    def romanToInt(self, s: str) -> int:
        def value(ch):
            if ch == 'M':
                return 1000
            elif ch == 'D':
                return 500
            elif ch == 'C':
                return 100
            elif ch == 'L':
                return 50
            elif ch == 'X':
                return 10
            elif ch == 'V':
                return 5
            elif ch == 'I':
                return 1
        sum = 0

        for i in range(len(s)):
            # Check if the next character is greater to know it the current is to be dedacted
            if i < len(s) - 1 and value(s[i]) < value(s[i + 1]):
                sum -= value(s[i])
            else:
                sum += value(s[i])
        return sum
