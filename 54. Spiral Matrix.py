class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        dxn = 0
        m = len(matrix)
        n = len(matrix[0])

        i = j = 0
        ceil, floor, r_wall, l_wall = 0, m - 1, n - 1, 0
        turned = False

        while True:
            while ceil <= i <= floor and r_wall >= j >= l_wall:
                answer.append(matrix[i][j])
                # Move forward
                i += int(math.sin(dxn))
                j += int(math.cos(dxn))
                # Resize boundaries after getting inside the allowable place
                if turned:
                    if dxn % (2 * math.pi) == math.pi:
                        ceil += 1
                        r_wall -= 1
                    elif dxn % (2 * math.pi) == 0:
                        floor -= 1
                        l_wall += 1
                    turned = False
            # Finish it we arrive at the destination
            if len(answer) == m * n:
                break
            # Return to previous position
            i -= int(math.sin(dxn))
            j -= int(math.cos(dxn))

            # Remove duplicate
            answer.pop()

            #Change direction
            dxn += math.pi / 2
            #Improve precision by making dxn = 0 after a full cycle
            if dxn % (2 * math.pi) == 0:
                dxn = 0
            # Communicate change of dxn
            turned = True

        return answer
