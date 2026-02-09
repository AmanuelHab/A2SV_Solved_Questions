class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)

        lst = [[element, count] for element, count in count_dict.items()]
        lst.sort(key=lambda x: -x[1])

        answer = []
        for i in range(k):
            answer.append(lst[i][0])
        return answer
