class Solution:
    def predict(self, p1, p2, nums, turn):
        if not nums:
            return p1 >= p2
        # if len(nums) == 1:
        #     return self.predict(p1 + nums[0], p2, [])
        if turn == 1:
        # If p1 chooses the first ele
            return self.predict(p1 + nums[0], p2, nums[1:], 2) or self.predict(p1 + nums[-1], p2, nums[:-1], 2)
        else:
            return self.predict(p1, p2 + nums[0], nums[1:], 1) and self.predict(p1, p2 + nums[-1], nums[:-1], 1)

        # return self.predict(p1 + first, p2 + maxi1, max)

    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.predict(0, 0, nums, 1)