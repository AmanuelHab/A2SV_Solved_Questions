class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        even_sum = sum(filter(lambda x: x%2 == 0, nums))
        for val, index in queries:
            new_val = val + nums[index]
            if new_val % 2 == 0 and nums[index] % 2 == 0:
                even_sum += val
            elif new_val % 2 == 0:
                even_sum += new_val
            elif nums[index] % 2 == 0:
                even_sum -= nums[index]

            nums[index] = new_val
            answer.append(even_sum)
        return answer
