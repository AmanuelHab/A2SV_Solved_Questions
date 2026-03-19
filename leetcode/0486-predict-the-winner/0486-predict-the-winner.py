class Solution:
    def predict(self, p1, p2, nums, turn):
        if not nums:
            return p1 >= p2

        # If it is p1's turn  
        if turn == 1:
            return self.predict(p1 + nums[0], p2, nums[1:], 2) or self.predict(p1 + nums[-1], p2, nums[:-1], 2)
        else:
            return self.predict(p1, p2 + nums[0], nums[1:], 1) and self.predict(p1, p2 + nums[-1], nums[:-1], 1)

    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.predict(0, 0, nums, 1)