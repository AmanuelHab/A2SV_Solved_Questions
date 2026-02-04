class Solution(object):
    def isCovered(self, ranges, left, right):
        mini = left
        min_covered = -1
        n = len(ranges)
        ranges.sort(key=lambda x: x[0])
        for i in range(n):
            if ranges[i][0] <= mini <= ranges[i][1]:
                min_covered = i
                break
            elif mini < ranges[i][0]:
                break
            
        if min_covered == -1:
            return False
        else:
            p = left
            while min_covered < n and p <= right:
                if ranges[min_covered][0] <= p <= ranges[min_covered][1]:
                    p += 1
                else:
                    min_covered += 1
            return True if p == right + 1 else False
