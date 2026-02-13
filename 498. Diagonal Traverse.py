class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = []
        m = len(mat)
        n = len(mat[0])
        end = m * n

        i = j = 0
        while True:
            even_traversal = ((i + j) % 2 ==  0)

            while 0 <= i < m and 0 <= j < n:
                # Move
                answer.append(mat[i][j])
                if even_traversal:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
            
            # Change direction
            if even_traversal:
                i += 1
                if j >= n:
                    j = min(j - 1, n - 1)
                    i += 1
            else:
                j += 1
                if i >= m:
                    i = min(i -1, m- 1)
                    j += 1
            
            if len(answer) >= end:
                break
        return answer
