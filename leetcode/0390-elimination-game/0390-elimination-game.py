class Solution:
    def lastRemaining(self, n: int) -> int:
        def recurse(x, step, count, left):
            if count == 1:
                return x
            if left or count % 2:
                x += step

            return recurse(x, step * 2, count // 2, not left)
        return recurse(1, 1, n, True)