class Solution:
    def customSortString(self, order: str, s: str) -> str:
        precedence = dict()
        precede = 0
        for ch in order:
            precedence[ch] = precede
            precede += 1

        def customSort(ch):
            return precedence.get(ch, float('inff'))

        return "".join(sorted(s, key=customSort))
