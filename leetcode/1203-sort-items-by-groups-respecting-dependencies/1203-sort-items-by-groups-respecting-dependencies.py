class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Build dependency graph for groups and for items
        graph = [[] for _ in range(n)] # for items
        group_dependency = [set() for _ in range(m+1)]# for groups
        group_items = [[] for _ in range(m+1)] # bundle items with the same group
        for i in range(n):
            group_items[group[i]].append(i)
            
        indegree = [0] * n
        for i in range(n):
            for j in range(len(beforeItems[i])):
                item = beforeItems[i][j]
                graph[item].append(i)
                indegree[i] += 1
                if group[item] != -1 and group[item] != group[i]:
                    group_dependency[group[item]].add(group[i])
                    
        # Order groups with their dependancy
        indegreeG = [0] * (m+1)
        for i in range(m+1):
            for g in group_dependency[i]:
                indegreeG[g] += 1
                
        groupSet = set(group)
        q = deque([i for i in range(-1,m) if indegreeG[i] == 0 and i in groupSet])
        group_order = []
        while q:
            g = q.popleft()
            group_order.append(g)
            for child in group_dependency[g]:
                indegreeG[child] -= 1
                if indegreeG[child] == 0:
                    q.append(child)
                    
        if len(set(group_order)) != len(groupSet):
            return []

        # Visit each group as per the above group order
        def bfs(g):
            q = deque([i for i in group_items[g] if indegree[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 0 and group[child] == g:
                        q.append(child)
            return order
            
        full_order = []

        # Add independent items(with no group) first
        q = deque([i for i in range(n) if group[i] == -1 and indegree[i] == 0])
        while q:
            node = q.popleft()
            full_order.append(node)
            indegree[node] -= 2
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0 and group[child] == -1:
                    q.append(child)
                    
        # Add the rest as per the group order
        for g in group_order:
            items = group_items[g]
            gOrder = bfs(g)
            
            if g != -1 and len(gOrder) != len(items):
                return []
            full_order.extend(gOrder)
        return full_order