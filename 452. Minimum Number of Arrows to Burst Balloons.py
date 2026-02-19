class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x : (x[0], x[1]))
        print(points)

        arrows = 1
        i = 1
        prev_start = points[0][0]
        prev_end = points[0][1]
        
        while i < n:
            # if the current start > previous end
            if points[i][0] > prev_end:
                arrows += 1
                prev_end = points[i][1]
                prev_start = points[i][0]
            else:
                prev_end = min(prev_end, points[i][1])
                prev_start = max(prev_start, points[i][0])
                
            i += 1
                
        return arrows
