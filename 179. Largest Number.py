class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        strs.sort(key=cmp_to_key(compare))
        answer = "".join(strs)
        if answer[0] == '0':
            return '0'
        else:
            return answer 
