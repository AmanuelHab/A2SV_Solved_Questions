class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ch_ransom = Counter(ransomNote)
        ch_magazine = Counter(magazine)

        for ch, count in ch_ransom.items():
            if count > ch_magazine[ch]:
                return False
        return True
