from collections import deque
def solve():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().strip())

    DAG = [set() for _ in range(26)]
    def code(ch): return ord(ch) - ord('a')
    def decode(x): return chr(x + ord('a'))

    indegree = [0] * 26
    for i in range(n-1):
        for j in range(i+1, n):
            min_l = min(len(words[i]), len(words[j]))
                # continue
            for k in range(min_l):
                if words[i][k] != words[j][k]:
                    DAG[code(words[i][k])].add(code(words[j][k]))
                    break
            else:
                if len(words[i]) > len(words[j]):
                    return "Impossible"

    for i in range(26):
        for dest in DAG[i]:
            indegree[dest] += 1
        
    q = deque([i for i in range(26) if indegree[i] == 0])
    order = []
    while q:
        node = q.popleft()
        order.append(decode(node))

        for child in DAG[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)
    if len(order) != 26:
        # print("".join(order))
        return "Impossible"
    return "".join(order)
print(solve())