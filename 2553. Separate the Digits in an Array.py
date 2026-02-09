class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            answer.extend(map(int, list(str(num))))
        return answer
