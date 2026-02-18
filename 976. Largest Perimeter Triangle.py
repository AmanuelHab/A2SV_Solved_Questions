class Solution:
    def triangleCanBeFormed(self, a:[int], b: [int], c:[int]) -> bool:
        if a + b > c and a + c > b and b + c > a:
            return True
        return False
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        # Sort the numbers so that the larger possible triangles can be at the end
        nums.sort()

        max_perimeter = 0
        for i in range(n - 2):
            # If triangle can be formed from the numbers upgrade the maximum perimeter
            if self.triangleCanBeFormed(nums[i], nums[i + 1], nums[i + 2]):
                max_perimeter = max((nums[i] + nums[i + 1] + nums[i + 2]), max_perimeter)

        return max_perimeter
