class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        # if citations[-1] == 0:
        #     return 0
        low = 0
        high = n
        while low < high:
            mid = (low + high) // 2
            if n - mid <= citations[mid]:
                high = mid
            else:
                low = mid + 1
        return n - high