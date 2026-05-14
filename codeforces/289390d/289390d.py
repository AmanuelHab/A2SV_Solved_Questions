class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.check_point = list(range(n))

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return 
        if self.size[rootX] < self.size[rootY]:
            rootY, rootX = rootX, rootY
        self.size[rootX] += self.size[rootY]
        self.parent[rootY] = rootX
        
    def ask(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        return rootX == rootY
    
n, m, q = map(int, input().split())
uf = UnionFind(n)
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u,v))

operations = []
Set = set()
for _ in range(q):
    cmd, * nums = input().split()
    u, v = map(int, nums)
    u -= 1
    v -= 1
    if cmd == 'cut':
        Set.add((u,v))
        Set.add((v,u))
    operations.append([cmd, [u,v]])

# Connect uncut edges
for edge in edges:
    if edge not in Set:
        uf.union(edge[0], edge[1])

response = []
operations.reverse()
for cmd, nums in operations:
    x, y = nums
    if cmd == 'ask':
        if uf.ask(x, y):
            response.append("YES")
        else:
            response.append("NO")
    else:
        uf.union(x,y)

response.reverse()
for res in response:
    print(res)