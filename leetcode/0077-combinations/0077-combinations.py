class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combo = []

        def generate(arr, n, k):
            if k == 0:
                combo.append(arr)
                return 
            starter = 1
            if arr:
                starter = arr[-1] + 1
            for i in range(starter, n + 1):
                if i not in arr:
                    generate(arr + [i], n, k - 1)
        generate([], n, k)
        return combo