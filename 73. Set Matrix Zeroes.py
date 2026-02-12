class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # Document the columns and rows to nullify
        columns = set()
        rows = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    columns.add(j)
                    rows.add(i)

        # Modify based on the documentation
        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
