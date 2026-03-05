def getValue(i, j):
    if board[i][j] == '#':
        return [0, 0, 0, 0]
    N = W = S = E = 0
    if i > 0 and board[i - 1][j] == '.':
        N += 1
    if j > 0 and board[i][j - 1] == '.':
        W += 1
    if i < height - 1 and board[i + 1][j] == '.':
        S += 1
    if j < width - 1 and board[i][j + 1] ==  '.':
        E += 1
    return [N, W, S, E]

N = [[0] * (width + 1) for _ in range(height + 1)]
W = [[0] * (width + 1) for _ in range(height + 1)]
S = [[0] * (width + 2) for _ in range(height + 2)]
E = [[0] * (width + 2) for _ in range(height + 2)]
for i in range(height):
    for j in range(width):
        n, w, s, e = getValue(i,j)
        N[i + 1][j + 1] = n
        W[i + 1][j + 1] = w
        S[i + 1][j + 1] = s
        E[i + 1][j + 1] = e

# Prefix sum for N, E, W & S
for i in range(1, height + 1):
    for j in range(1, width + 1):
        N[i][j] += N[i - 1][j] + N[i][j - 1] - N[i - 1][j - 1]
        W[i][j] += W[i - 1][j] + W[i][j - 1] - W[i - 1][j - 1]
        S[i][j] += S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1]
        E[i][j] += E[i - 1][j] + E[i][j - 1] - E[i - 1][j - 1]

q = int(input())
for _ in range(q):
    start_i, start_j, end_i, end_j = map(int, input().split())

    answer = 0
    North = N[end_i][end_j] - N[start_i - 1][end_j] - N[end_i][start_j - 1] + N[start_i - 1][start_j - 1]
    West = W[end_i][end_j] - W[start_i - 1][end_j] - W[end_i][start_j - 1] + W[start_i - 1][start_j - 1]
    South = S[start_i - 1][end_j] - S[start_i - 2][end_j] - S[start_i - 1][start_j - 1] + S[start_i - 2][start_j - 1]
    East = E[end_i][start_j - 1] - E[end_i][start_j - 2] - E[start_i - 1][start_j - 1] + E[start_i - 1][start_j - 2]
    
    answer = North + West - South - East

    print(answer)