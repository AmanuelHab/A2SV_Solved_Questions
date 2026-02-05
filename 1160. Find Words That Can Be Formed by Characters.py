class Solution(object):
    def countCharacters(self, words, chars):
        chars_c = defaultdict(int)
        for ch in chars:
            chars_c[ch] += 1
        sum = 0
        for word in words:
            word_c = dict()
            for ch in word:
                word_c[ch] = word_c.get(ch, 0) + 1
            good = True
            for char in word_c:
                if word_c[char] > chars_c[char]:
                    good = False
                    break
            if good:
                sum += len(word)

        return sum
