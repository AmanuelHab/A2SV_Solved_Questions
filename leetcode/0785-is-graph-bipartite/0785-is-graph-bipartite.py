class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        def dfs(node, g):
            if not group[node]:
                group[node] = g
            elif group[node] != g:
                return False
            if node in visited:
                return True
             
            visited.add(node)
            for nbr in graph[node]:
                if not dfs(nbr, -g):
                    return False
            return True

        visited = set()
        group = [None] * n
        for i in range(n):
            if i not in visited and not dfs(i, 1):
                return False
        return True