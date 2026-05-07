class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapify(max_heap)

        while len(max_heap) > 1:
            y = -heappop(max_heap)
            x = -heappop(max_heap)
            if x != y:
                heappush(max_heap, x - y)
        if not max_heap:
            return 0
        return -max_heap[0]