class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        ch_count = [0] * 26
        left = total_count = 0
        max_len = 1
        for right in range(n):
            ch_count[ord(s[right]) - ord('A')] += 1
            total_count += 1
            # If k < length - max_freq
            while k < right - left + 1 - max(ch_count) and left < n:
                ch_count[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
