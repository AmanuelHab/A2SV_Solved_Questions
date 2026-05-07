class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr=[]
        for row in matrix:
            for num in row:
                if len(arr) < k:
                    heappush(arr, -num)
                else:
                    heappushpop(arr, -num)
        return -arr[0]