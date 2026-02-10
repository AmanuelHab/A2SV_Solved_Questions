class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)

        for ch, count in s_count.items():
            if t_count[ch] != count:
                return False
        return True
