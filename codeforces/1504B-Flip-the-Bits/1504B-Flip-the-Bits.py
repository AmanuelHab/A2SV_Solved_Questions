for _ in range(int(input())):
    n = int(input())
    a = list(map(int, list(input())))
    b = list(map(int, list(input())))

    indices = [0]
    zeros = ones = 0
    for i in range(n):
        if a[i]:
            ones += 1
        else:
            zeros += 1
        if ones == zeros:
            indices.append(i + 1)
    
    for i in range(len(indices) - 1):
        a_part = a[indices[i]: indices[i + 1]]
        b_part = b[indices[i]: indices[i + 1]]

        b_flip = [num ^ 1 for num in b_part]
        if a_part != b_part and a_part != b_flip:
            print("NO")
            break
    else:
        a_part = a[indices[-1]:]
        b_part = b[indices[-1]:]
        if a_part != b_part:
            print("NO")
        else:
            print("YES")