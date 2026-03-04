class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        final_shift = [0] *(n + 1)
        for shift in shifts:
            l, r, key = shift
            if key:
                final_shift[l] += 1
                final_shift[r + 1] -= 1
            else:
                final_shift[l] -= 1
                final_shift[r + 1] += 1
        for i in range(n):
            final_shift[i + 1] += final_shift[i]
            
        final_s = []
        for i in range(n):
            ch_num = ord(s[i]) - ord('a')
            final_s.append(chr((ch_num + final_shift[i]) % 26 + ord('a')))
        return "".join(final_s)