class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        answers = []
        def generate(s, arr):
            if not s:
                answers.append(" ".join(arr))
                return
            for i in range(len(s) + 1):
                if s[:i] in wordDict:
                    print(s[:i])
                    generate(s[i:], arr + [s[:i]])

        generate(s, [])
        return answers