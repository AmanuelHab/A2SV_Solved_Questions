class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canCary(capacity):
            total = 0
            day = 1
            i = 0
            while i < len(weights):
                total += weights[i]
                if capacity == 3:
                    print(total, weights[i], day)
                if total > capacity:
                    total = 0
                    day += 1
                    if day > days:
                        return False
                else:
                    i += 1
            return True

        left = 1
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if not canCary(mid):
                left = mid + 1
            else:
                right = mid
        return right