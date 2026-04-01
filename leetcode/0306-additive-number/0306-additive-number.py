class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        answers = []
        def generate(s, arr):
            if not s:
                return True
            boolean = False
            for i in range(1, len(s) + 1):
                ss = s[:i]
                if len(ss) > 1 and ss[0] == '0':
                    continue
                int_ss = int(ss)
                if len(arr) > 1:
                    if int_ss == arr[-1] + arr[-2]:
                        boolean = boolean or generate(s[i:], arr + [int_ss])
                elif i < len(s):
                    if int_ss <= int(s[i:]):
                        boolean = boolean or generate(s[i:], arr + [int_ss])
            return boolean
        return generate(num, [])
        