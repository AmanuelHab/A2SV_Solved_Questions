from collections import defaultdict 
 
for _ in range(int(input())):
    n = int(input())
    lst = list(input())
 
    indices_of_a = []
    for i in range(n):
        if lst[i] == 'a':
            indices_of_a.append(i)
 
    if len(indices_of_a) < 2:
        print(-1)
        continue
 
    answer = float('inf')
 
    for start_ind in range(len(indices_of_a)):
        i = indices_of_a[start_ind]
        ch_count = defaultdict(int)
        j = i
 
        for k in range(start_ind,min(start_ind + 8, len(indices_of_a))):
            next_a_ind = indices_of_a[k]
            while j <= next_a_ind:
                ch_count[lst[j]] += 1
                j += 1
            if ch_count['a'] > ch_count['b'] and ch_count['a'] > ch_count['c'] and ch_count['a'] != 1:
                answer = min(answer, j - i)
                break
 
    print(answer if answer != float('inf') else -1)
