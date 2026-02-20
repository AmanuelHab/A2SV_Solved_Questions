for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    operations = []
    #Bubble sort a
    for i in range(n):
        for j in range(1, n - i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                # Record operation
                operations.append([1, j])
    
    #Bubble sort b
    for i in range(n):
        for j in range(1, n - i):
            if b[j - 1] > b[j]:
                b[j - 1], b[j] = b[j], b[j - 1]
                # Record operation
                operations.append([2, j])

    # Swap 
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            # Record operation
            operations.append([3, i + 1])

    # Print answers
    ops = len(operations)
    print(ops)
    if ops:
        for oper in operations:
            print(*oper)
