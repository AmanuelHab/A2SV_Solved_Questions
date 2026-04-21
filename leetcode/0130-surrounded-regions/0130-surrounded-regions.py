class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        dxn = [(-1,0), (1,0), (0,-1), (0,1)]
        def safe(i,j):
            return 0 <= i < m and 0 <= j < n and (i,j) not in visited and board[i][j] == 'O'
        def visit(i,j):
            visited.add((i,j))

            for x, y in dxn:
                new_i = i + x
                new_j = j + y
                if safe(new_i, new_j):
                    visit(new_i, new_j)
        visited = set()

        #Visit unsurrounded regions
        for j in range(n):
            if safe(0,j):
                visit(0, j)
            if safe(m-1,j):
                visit(m-1, j)
        for i in range(m):
            if safe(i,0):
                visit(i, 0)
            if safe(i,n-1):
                visit(i, n-1)
        
        def capture(i,j):
            visited.add((i,j))
            board[i][j] = 'X'

            for x, y in dxn:
                new_i = i + x
                new_j = j + y
                if safe(new_i, new_j):
                    capture(new_i, new_j)
        
        # Modify the surrounded regions
        for i in range(m):
            for j in range(n):
                if safe(i,j):# and (i,j) not in visited:
                    capture(i,j)
        
        
        """
        Do not return anything, modify board in-place instead.
        """
        