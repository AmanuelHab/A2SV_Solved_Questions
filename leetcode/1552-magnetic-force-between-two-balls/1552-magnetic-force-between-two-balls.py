class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        low = 1
        high = position[-1] - position[0]

        def check(n):
            i = 0
            cnt = 0
            while i < len(position):
                i = bisect_left(position, position[i] + n)
                cnt += 1
            return cnt >= m
        mini = 0
        while low <= high:
            mid = low + (high - low) // 2
            
            if check(mid):
                low = mid+1
            else:
                high = mid - 1
        return high



        # def distribute(left, right, x):
        #     if x <= 0:
        #         return
            
        #     mid = left + (right - left) // 2
        #     # The mid consumes one ball
        #     position[mid] = -position[mid]
        #     x -= 1

        #     distribute(left, mid - 1, x)
        #     distribute(mid + 1, right, x)

        # distribute(0, len(position) - 1, m - 2)
        # position[0] = -position[0]
        # position[-1] = -position[-1]
        
        # min_dist = float('inf')
        # l = 0
        # for r in range(len(position)):
        #     if l != r and position[l] < 0 and position[r] < 0:
        #         dist = abs(position[l] - position[r])
        #         min_dist = min(dist, min_dist)
        #         l = r
        # return min_dist