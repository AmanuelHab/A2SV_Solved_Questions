class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        dxn = [(-1, 0), (1,0), (0,-1), (0,1)]
        reach = [[1]* n for _ in range(m)]
        def safe(i,j):
            return 0 <= i < m and 0 <= j < n and (i,j) not in visited
        def mark(i,j, f):
            # if (i,j) in visited:
            #     return
            visited.add((i,j))
            # if i == m-1 or j == n-1:
            #     reach[i][j] *= f
            reach[i][j] *= f
            for x, y in dxn:
                new_i = i + x
                new_j = j + y
                if safe(new_i, new_j) and heights[i][j] <= heights[new_i][new_j]:
                    mark(new_i,new_j, f)
        visited = set()
        for i in range(m):
            mark(i,0,2)
        for j in range(n):
            mark(0,j,2)
        visited.clear()
        for i in range(m):
            mark(i,n-1,3)
        for j in range(n):
            mark(m-1,j,3)
        mark(0,0,2)
        mark(m-1, n-1, 3)
        print(reach)

        result = []
        for i in range(m):
            for j in range(n):
                if reach[i][j] % 2 == reach[i][j] % 3 == 0:
                    result.append([i,j]) 

        return result




        # def safeA(i,j):
        #     return 0 <= i < m and 0 <= j < n and ((i,j) not in visitedA or reachA[i][j] % 2 == 0)
        # def safeP(i,j):
        #     return 0 <= i < m and 0 <= j < n and ((i,j) not in visitedP or reachP[i][j] % 3 == 0)

        # reachA = [[1]*n for _ in range(m)]
        # reachP = [[1]*n for _ in range(m)]
        # def reachesAtlantic(i,j):
        #     # print("A:", i, j)
        #     visitedA.add((i,j))
        #     if reachA[i][j] % 2 == 0:
        #         return True
        #     if i == m-1 or j == n-1:
        #         reachA[i][j] *= 2
        #         return True
            
        #     for x,y in dxn:
        #         new_i = i + x
        #         new_j = j + y

        #         if (safeA(new_i, new_j) and heights[i][j] >= heights[new_i][new_j]):
        #             if reachesAtlantic(new_i,new_j):
        #                 reachA[new_i][new_j] *= 2
        #                 return True
        #     return False
            
        # def reachesPacific(i,j):
        #     # print("P: ", i,j)
        #     visitedP.add((i,j))
        #     if reachP[i][j] % 3 == 0:
        #         return True
        #     if i == 0 or j == 0:
        #         reachP[i][j] *= 3
        #         return True
            
        #     for x, y in dxn:
        #         new_i = i + x
        #         new_j = j + y

        #         if safeP(new_i, new_j) and heights[i][j] >= heights[new_i][new_j]:
        #             if reachesPacific(new_i, new_j):
        #                 reachP[new_i][new_j] *= 3
        #                 return True
        #     return False

        # visitedA = set()
        # visitedP = set()
        # result = []
        
        # for i in range(m):
        #     for j in range(n):
        #         if reachesAtlantic(i,j):
        #             reachA[i][j] *= 2
        #         if reachesPacific(i,j):
        #             reachP[i][j] *= 3
                    
        # for i in range(m):
        #     for j in range(n):
        #         if reachesAtlantic(i,j) and reachesPacific(i,j):
        #             result.append([i,j]) 

        # return result