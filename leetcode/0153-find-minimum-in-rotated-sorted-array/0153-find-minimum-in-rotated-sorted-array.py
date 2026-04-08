class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Tournament
        def compete(left, right):
            if left == right:
                return nums[left]
            mid = left + (right - left) // 2
            left_winner = compete(left, mid)
            right_winner = compete(mid + 1, right)
            return min(left_winner, right_winner)
        return compete(0, len(nums)-1)