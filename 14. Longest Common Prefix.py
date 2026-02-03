class Solution(object):
    def longestCommonPrefix(self, strs):
        s = ""
        min_len = len(min(strs, key = lambda s: len(s)))
        for i in range(min_len):
            char = strs[0][i]
            finished = False
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    finished = True
                    break
            else: 
                s += char
            if finished:
                break
        return s
        """
        :type strs: List[str]
        :rtype: str
        """
        
