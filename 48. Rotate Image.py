class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(n):
                if i - j > 0:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse rows
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

        """
        Do not return anything, modify matrix in-place instead.
        """
