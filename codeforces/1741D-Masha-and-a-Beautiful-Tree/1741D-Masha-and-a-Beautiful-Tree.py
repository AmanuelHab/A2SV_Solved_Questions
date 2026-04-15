import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque

numb = lambda: int(input())
lst = lambda: list(map(int, input().split()))
# yn = lambda condition: "YES" if condition else "NO"

def solve():
    n = numb()
    tree = lst()
    if n == 1:
        return 0
    def mergeswap(arr):
        nonlocal swaps
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left = mergeswap(arr[:mid])
        right = mergeswap(arr[mid:])

        if left[-1] < right[0]:
            return left + right
        swaps += 1
        return right + left
    swaps = 0
    new_arr = mergeswap(tree)

    if new_arr == sorted(tree):
        return swaps
    return -1

for _ in range(numb()):
    print(solve())