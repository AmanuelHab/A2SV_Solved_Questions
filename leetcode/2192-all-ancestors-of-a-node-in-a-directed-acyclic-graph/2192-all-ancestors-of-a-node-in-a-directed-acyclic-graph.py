class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Construct graph and indegree
        graph = [[] for _ in range(n)]
        ancestors = [set() for _ in range(n)]
        indegree = [0] * n
        for u,v in edges:
            indegree[v] += 1
            graph[u].append(v)
            ancestors[v].add(u)
            
        q = deque([i for i in range(n) if indegree[i] == 0])
        while q:
            parent = q.popleft()
            for child in graph[parent]:
                ancestors[child].update(ancestors[parent])
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        for i in range(n):
            ancestors[i] = sorted(list(ancestors[i]))
        return ancestors