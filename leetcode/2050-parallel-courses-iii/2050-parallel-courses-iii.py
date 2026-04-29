class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * (n)
        for pre, crs in relations:
            graph[pre-1].append(crs-1)
            indegree[crs-1] += 1
            
        q = deque([i for i in range(n) if indegree[i] == 0])
        timeB = [0] * n
        while q:
            pre = q.popleft()
            for crs in graph[pre]:
                timeB[crs] = max(timeB[crs], time[pre] + timeB[pre])
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
                    
        for i in range(n):
            timeB[i] += time[i]
            
        return max(timeB)