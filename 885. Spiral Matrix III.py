class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Simulate the clockwise walk
        total = rows * cols
        answer = []
        i, j = rStart, cStart
        walk = 1
        while len(answer) < total:
            # Move East
            for k in range(1, walk + 1):
                # Record proper indices on the walk
                if 0 <= i < rows and 0 <= j < cols:
                    answer.append([i, j])
                j += 1
            # Move South
            for k in range(1, walk + 1):
                # Record proper indices on the walk
                if 0 <= i < rows and 0 <= j < cols:
                    answer.append([i, j])
                i += 1
            walk += 1
            #Move West
            for k in range(1, walk + 1):
                # Record proper indices on the walk
                if 0 <= i < rows and 0 <= j < cols:
                    answer.append([i, j])
                j -= 1
            # Move North
            for k in range(1, walk + 1):
                # Record proper indices on the walk
                if 0 <= i < rows and 0 <= j < cols:
                    answer.append([i, j])
                i -= 1
            walk += 1
        return answer
