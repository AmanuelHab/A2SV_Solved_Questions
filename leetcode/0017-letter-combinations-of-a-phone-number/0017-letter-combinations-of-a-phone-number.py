class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_ch = {
            2: ['a', 'b','c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        combo = []
        def combine(s, digits):
            if not digits:
                combo.append(s)
                return
            digit = int(digits[0])
            for ch in digit_ch[digit]:
                combine(s + ch, digits[1:])
        combine("", digits)
        return combo