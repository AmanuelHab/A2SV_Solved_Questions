class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()

        left, right = 0, n - 2
        total = 0
        while left < right:
            total += piles[right]
            left += 1
            right -= 2
        return total
