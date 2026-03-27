class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers = []
        def generate(board, i):
            set_value = tuple(["".join(row) for row in board])
            if i == n:
                answers.append(list(set_value))
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
        
        for i in range(len(answers)):
            for j in range(n):
                answers[i][j] = answers[i][j].replace('#', '.')

        return answers