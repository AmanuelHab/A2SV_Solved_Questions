for _ in range(int(input())):
    n, x, k = map(int, input().split())
    command = input()

    first_zero = False
    second_zero = False

    cummulative_move = [None] * n
    cummulative_move[0] = 1 if command[0] == 'R' else -1
    for i in range(1, n):
        move = 1 if command[i] == 'R' else -1
        cummulative_move[i] = cummulative_move[i - 1] + move

    for i in range(n):
        if cummulative_move[i] + x == 0:
            first_zero = i
            break

    if type(first_zero) is bool:
        print(0)
        continue

    
    for i in range(n):
        if cummulative_move[i] == 0:
            second_zero = i
            break
    if type(second_zero) is bool:
        print(1)
        continue

    print(((k - first_zero - 1) // (second_zero + 1))  + 1)
