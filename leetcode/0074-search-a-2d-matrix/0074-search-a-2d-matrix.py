class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # Find the row
        low = 0
        high = m-1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        row = high
        print(row)

        # Find the column
        low = 0
        high = n-1
        ind = -1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[row][mid] == target:
                ind = mid
                break
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        print(ind)
        return ind != -1