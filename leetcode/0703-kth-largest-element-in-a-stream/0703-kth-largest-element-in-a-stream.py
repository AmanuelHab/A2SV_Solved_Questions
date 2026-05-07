class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = sorted(nums, reverse=True)
        self.heap = nums[:k]
        heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heappushpop(self.heap, val)
        else:
            heappush(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)