class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def canSpanAll(dist):
            i = 0
            for heater in heaters:
                while i < len(houses) and heater - dist <= houses[i] <= heater + dist:
                    i += 1
            if i == len(houses):
                return True
            return False

        low = 0
        high = max(houses[-1], heaters[-1]) - houses[0] + 1
        while low < high:
            mid = (low + high) // 2
            if not canSpanAll(mid):
                low = mid + 1
            else:
                high = mid
        return high