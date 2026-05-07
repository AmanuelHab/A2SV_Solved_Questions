class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights) - 1
        heap = []
        for i in range(n):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if len(heap) < ladders:
                    heappush(heap, diff)
                else:
                    # Use bricks
                    x = heappushpop(heap, diff)
                    bricks -= x
                    if bricks < 0:
                        return i
        return n