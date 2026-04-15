class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def check(n):
            total = 0
            for candy in candies:
                total += candy // n
            return total >= k

        low = 1
        high = max(candies)

        while low <= high:
            mid = low + (high - low) // 2

            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high

        # total = sum(candies)
        # n = len(candies)
        # if k > total:
        #     return 0
        # divisor = min(min(candies), total // k)
        # print(divisor)
        # # candies.sort()
        # count = 0
        # for candy in candies:
        #     count += candy // divisor
        # if count == k:
        #     return divisor
        # return 0