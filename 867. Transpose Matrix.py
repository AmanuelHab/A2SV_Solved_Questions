class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        answer = []
        for i in range(n): # column
            column = []
            for j in range(m):
                column.append(matrix[j][i])
            answer.append(column)
        return answer
