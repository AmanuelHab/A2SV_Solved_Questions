class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i in range(n):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] < temp:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
                
            stack.append(i)

        return answer