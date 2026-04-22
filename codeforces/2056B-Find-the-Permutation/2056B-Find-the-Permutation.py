import sys
input = sys.stdin.readline
from collections import defaultdict, Counter, deque

num = lambda: int(input())
nums = lambda: list(map(int, input().strip().split()))
lst = lambda: list(input())
def mtrx(m):
    matrix = []
    for i in range(m):
        row = input().strip()
        matrix.append(row)
    return matrix

def solve():
    n = num()
    # arr = [0] * n

    mat = mtrx(n)

    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1,n):
            if mat[i][j] == '1':
                graph[i+1].append(j+1)
            else:
                graph[j+1].append(i+1)
    # print(graph)
    visited = set()
    order = []
    def dfs(node):
        visited.add(node)
        for nbr in sorted(graph[node],reverse=True):
            if nbr not in visited:
                dfs(nbr)
        order.append(node)
        # print(order)
    for i in range(1, n+1):
        if i not in visited:
            dfs(i)
    order.reverse()
    print(*order)
    
for _ in range(num()):
    solve()