class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        candidates = []
        def generate(s, ind):
            if ind >= n:
                candidates.append(s)
                return
            
            for i in range(1, 10):
                s_i = str(i)
                if pattern[ind] == 'I':
                    if s_i not in s and int(s[-1]) < i:
                        generate(s + s_i, ind + 1)
                else:
                    if s_i not in s and int(s[-1]) > i:
                        generate(s + s_i, ind + 1)
            
        for i in range(1, 10):
            generate(str(i), 0)
        print(len(candidates))

        return min(candidates) if candidates else 0