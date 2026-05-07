import sys 
from heapq import heapify, heappush, heappop, heappushpop, heapreplace
input = sys.stdin.readline

num = lambda: int(input())
nums = lambda: list(map(int, input().strip().split()))
lst = lambda: list(input().strip())

def solve():
    n = num()
    heap = []
    log = []
    for _ in range(n):
        s = input().strip()
        op = s.split()
        if len(op) == 1:
            if not heap:
                log.append('insert 0')
                heappush(heap, 0)
            log.append(s)
            heappop(heap)
        else:
            operation, x = op
            x = int(x)
            if operation == 'insert':
                heappush(heap, x)
                log.append(s)
            else:
                while heap and heap[0] < x:
                    log.append('removeMin')
                    heappop(heap)
                
                if not heap or heap and heap[0] > x:
                    log.append(f'insert {x}')
                    heappush(heap, x)

                log.append(s)

    print(len(log))
    for line in log:
        print(line)
        
solve()