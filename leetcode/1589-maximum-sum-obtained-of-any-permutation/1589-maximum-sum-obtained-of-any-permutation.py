class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        nums.sort()

        request_board = [0] * (n + 1)

        for left, right in requests:
            request_board[left] += 1
            request_board[right + 1] -= 1
        for i in range(n):
            request_board[i + 1] += request_board[i]
        
        count = Counter(request_board)
        count[request_board[-1]] -= 1
        count = dict(sorted(count.items(), reverse=True))
        total = 0
        for num, freq in count.items():
            for _ in range(freq):
                total += nums.pop() * num
        return total % (10**9 + 7)