class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y, z):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return 0
        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX
        self.size[rootX] += self.size[rootY]
        self.parent[rootY] = rootX
        return z
    
n, m = map(int, input().split())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
edges.sort(key= lambda x: x[2])

uf = UnionFind(n)
count = 0
for u, v, w in edges:
    u -= 1
    v -= 1
    count += uf.union(u, v, w)
print(count)