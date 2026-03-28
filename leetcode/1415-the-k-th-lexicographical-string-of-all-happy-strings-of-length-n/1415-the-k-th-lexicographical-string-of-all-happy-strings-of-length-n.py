class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        answer = []
        def generate(s, n):
            nonlocal k
            if n == 0:
                k -= 1
                if k == 0:
                    answer.append(s)
                return
                
            if k < 0:
                return
                
            for ch in 'abc':
                if len(s):
                    if ch != s[-1]:
                        generate(s + ch, n - 1)
                else:
                    generate(s + ch, n - 1)
        generate("", n)
        return answer[0] if answer else ""