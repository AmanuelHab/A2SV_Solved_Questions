from collections import deque
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for i in range(n):
        graph[i].append(arr[i]-1)
        indegree[arr[i]-1] += 1
    
    q = deque([ i for i in range(n) if indegree[i] == 0])
    # print(indegree, q)
    if not q:
        print(2)
        continue
    years = 2
    while q:
        new_q = deque()
        for node in q:
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    new_q.append(child)
        q = new_q
        years += 1

    print(years)