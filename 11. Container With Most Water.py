class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0, n - 1
        max_area = 0
        while left < right:
            # Calculate the current possible area
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            # Go optimal
            # If step is favorable
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
