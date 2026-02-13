class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_set = set()
        word_char = dict()
        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if word in word_char and word_char[word] != ch:
                return False
            elif word not in word_char and ch in char_set:
                return False
                
            char_set.add(ch)
            word_char[word] = ch

        return True
