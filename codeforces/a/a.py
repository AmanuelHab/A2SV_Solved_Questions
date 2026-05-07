import sys
input = sys.stdin.readline
from collections import defaultdict, Counter, deque

num = lambda: int(input())
nums = lambda: list(map(int, input().strip().split()))
lst = lambda: list(input().strip())

def solve():
    n = num()
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = nums()
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(node):
        d = -1
        q = deque([node])
        visited = [False] * (n+1)
        while q:
            new_q = deque()
            for node in q:
                for nbr in graph[node]:
                    if not visited[nbr]:
                        new_q.append(nbr)
                        visited[nbr] = True
            d += 1
            if not new_q:
                return [q[-1], d]
            q = new_q
    last, dis = bfs(1)
    no, d = bfs(last)
    print(d * 3)

solve()