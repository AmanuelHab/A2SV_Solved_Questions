class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_dict = Counter(nums)
        n = len(nums)

        answer = []
        for num, count in count_dict.items():
            if count > (n / 3):
                answer.append(num)
        return answer
