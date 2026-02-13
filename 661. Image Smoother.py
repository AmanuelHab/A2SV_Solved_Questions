class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        copy_img = copy.deepcopy(img)
        row_len = len(img)
        col_len = len(img[0])

        for i in range(row_len):
            for j in range(col_len):
                summ = 0
                neighbors = 0
                # 1
                if i - 1 >= 0 and j - 1 >= 0:
                    summ += img[i - 1][j - 1]
                    neighbors += 1
                # 2
                if i - 1 >= 0:
                    summ += img[i - 1][j]
                    neighbors += 1
                # 3
                if i - 1 >= 0 and j + 1 < col_len:
                    summ += img[i - 1][j + 1]
                    neighbors += 1
                # 4
                if j - 1 >= 0:
                    summ += img[i][j - 1]
                    neighbors += 1
                #5
                summ += img[i][j]
                neighbors += 1
                #6
                if j + 1 < col_len:
                    summ += img[i][j + 1]
                    neighbors += 1
                #7
                if i + 1 < row_len and j - 1 >= 0:
                    summ += img[i + 1][j - 1]
                    neighbors += 1
                #8
                if i + 1 < row_len:
                    summ += img[i + 1][j]
                    neighbors += 1
                #9
                if i + 1 < row_len and j + 1 < col_len:
                    summ += img[i + 1][j + 1]
                    neighbors += 1
                
                copy_img[i][j] = summ // neighbors

        return copy_img
