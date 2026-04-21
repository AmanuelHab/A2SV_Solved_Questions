class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dxn = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def goodToGo(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == '1'

        def explore(i, j):
            grid[i][j] = '0'
            
            for x, y in dxn:
                new_i = i + x
                new_j = j + y
                if goodToGo(new_i, new_j):
                    explore(new_i, new_j)
                    
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]== '1':
                    explore(i,j)
                    count += 1
        return count