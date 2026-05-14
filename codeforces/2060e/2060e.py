class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

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
        return self.find(x) == self.find(y)
    
for _ in range(int(input())):
    n, m1, m2 = map(int, input().split())
    uf1 = UnionFind(n)
    uf2 = UnionFind(n)
    F = []
    for _ in range(m1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        F.append((u,v))
        # uf1.union(u,v)
    G = []
    for _ in range(m2):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G.append((u,v))
        uf2.union(u,v)

    count = 0
    # Count edges to be removed
    for u, v in F:
        if not uf2.ask(u,v):
            count += 1
        else:
            uf1.union(u,v)
    # Count edges to be added
    for u, v in G:
        if not uf1.ask(u,v):
            count += 1
            uf1.union(u,v)
    print(count)