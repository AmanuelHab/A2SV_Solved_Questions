class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = [None] * len(s)
        for i in range(len(indices)):
            index = indices[i]
            lst[index] = s[i]
        return "".join(lst)
