class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate90(copy):
            # Transpose
            for i in range(n):
                for j in range(n):
                    if i > j:
                        copy[i][j], copy[j][i] = copy[j][i], copy[i][j]
            # Flip 
            for i in range(n):
                for j in range(n // 2):
                    copy[i][j], copy[i][n - j- 1] = copy[i][n - j - 1], copy[i][j]
            return copy
        
        copy = []
        for row in mat:
            copy.append(row[:])
        for i in range(4):
            copy = rotate90(copy)
            if copy == target:
                return True
        return False
