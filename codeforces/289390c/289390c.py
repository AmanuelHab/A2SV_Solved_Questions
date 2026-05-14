class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.offset = [0] * n
        self.base = [0] * n

    def find(self, x):
        if x == self.parent[x]:
            return x
        par = self.parent[x]
        self.parent[x] = self.find(self.parent[x])
        self.offset[x] += self.offset[par]
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        # Make rootX the largest
        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX

        self.size[rootX] += self.size[rootY]
        self.parent[rootY] = rootX
        self.offset[rootY] = self.base[rootY] - self.base[rootX]

    def add(self, x, v):
        rootX = self.find(x)
        self.base[rootX] += v

    def get(self, x):
        rootX = self.find(x)
        return self.base[rootX] + self.offset[x]


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    cmd, *nums = input().split()
    nums = list(map(int, nums))
    if cmd == 'add':
        uf.add(nums[0]-1, nums[1])
    elif cmd == 'join':
        uf.union(nums[0]-1, nums[1]-1)
    else:
        print(uf.get(nums[0]-1))