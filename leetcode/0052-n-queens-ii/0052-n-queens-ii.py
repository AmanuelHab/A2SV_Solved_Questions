class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        def generate(board, i):
            nonlocal count
            if i >= n:
                count += 1
                return
            for j in range(n):
                if board[i][j] == '.':
                    new_board = [row[:] for row in board]
                    new_board[i][j] = 'Q'
                    for k in range(n):
                        for l in range(n):
                            if not (k == i and l == j):
                                if k == i or l == j or k + l == i + j or k - l == i - j:
                                    new_board[k][l] = '#'
                    generate(new_board, i + 1)
        board = [list('.' * n) for _ in range(n)]
        generate(board, 0)

        return count