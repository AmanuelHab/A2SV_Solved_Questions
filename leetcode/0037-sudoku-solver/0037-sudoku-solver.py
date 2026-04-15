class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Store counts in sets
        # Sets of each row
        row_set = [ set(row) for row in board]

        # Sets of each column
        col_set = []
        for j in range(9):
            Set = set()
            for i in range(9):
                if board[i][j] != '.':
                    Set.add(board[i][j])
            col_set.append(Set)

        # 2D array of sets of sub-boxes
        box_set = []
        for i in range(0, 9, 3):
            bxr_count = []
            for j in range(0, 9, 3):
                count = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] != '.':
                            count.add(board[k][l])
                bxr_count.append(count)
            box_set.append(bxr_count)

        answer = []
        def generate(row):
            nonlocal answer
            if row == 9:
                answer = [row[:] for row in board]
                return
            if answer: # Cut down further recursion if the answer is found
                return
                
            dot_found = False
            for j in range(9):
                if board[row][j] == '.':
                    dot_found = True
                    for num in '123456789':
                        if num not in row_set[row] and num not in col_set[j] and num not in box_set[row//3][j // 3]: # Set possible value
                            board[row][j] = num
                            row_set[row].add(num)
                            col_set[j].add(num)
                            box_set[row// 3][j// 3].add(num)

                            generate(row)
                            # Reset if the answer is not attainable
                            board[row][j] = "."
                            row_set[row].remove(num)
                            col_set[j].remove(num)
                            box_set[row// 3][j// 3].remove(num)
                            updated_dot = True
                    break
                    
            if not dot_found: # If the row is filled go to the next
                generate(row + 1)

        generate(0)
        # Rewrite the grid
        for i in range(9):
            for j in range(9):
                board[i][j] = answer[i][j]
        """
        Do not return anything, modify board in-place instead.
        """