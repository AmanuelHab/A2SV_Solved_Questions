class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        heap = []
        for word, count in word_count.items():
            heappush(heap, (-count, word))

        answer = []
        while k > 0:
            c, w = heappop(heap)
            answer.append(w)
            k -= 1

        return answer