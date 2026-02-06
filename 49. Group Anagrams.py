class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_book = defaultdict(list)

        for s in strs:
            anagram_book["".join(sorted(s))].append(s)

        answer = []
        for value in anagram_book.values():
            answer.append(value)
        return answer
