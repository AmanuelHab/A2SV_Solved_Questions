n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0
x = y = 0
a_ptr = b_ptr = 0

while a_ptr < n and b_ptr < m:
    if a[a_ptr] == b[b_ptr]:
        x = 1
        y = 1
        
        while b_ptr < m - 1 and b[b_ptr + 1] == a[a_ptr]:
            y += 1
            b_ptr += 1
        while a_ptr < n - 1 and a[a_ptr + 1] == b[b_ptr]:
            x += 1
            a_ptr += 1
        answer += x * y
        a_ptr += 1
        b_ptr += 1
    elif a[a_ptr] > b[b_ptr]:
        b_ptr += 1
    else:
        a_ptr += 1 
        
print(answer)
