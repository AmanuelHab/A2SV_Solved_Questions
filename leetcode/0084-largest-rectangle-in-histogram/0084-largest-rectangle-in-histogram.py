class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        max_area = 0
        for i in range(n):
            start = i
            while stack and stack[-1][1] > heights[i]:
                ind, h = stack.pop()
                max_area = max((i - ind) * h, max_area)
                start = ind
            stack.append((start, heights[i]))

        for _ in range(len(stack)):
            ind, h = stack.pop()
            max_area = max((n - ind) * h, max_area)

        return max_area