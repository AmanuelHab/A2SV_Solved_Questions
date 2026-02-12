matrix = []
i = j = 0
for k in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        i = k
        j = row.index(1)
        break
    matrix.append(row)
    
print(abs(2 - i) + abs(2 - j))
