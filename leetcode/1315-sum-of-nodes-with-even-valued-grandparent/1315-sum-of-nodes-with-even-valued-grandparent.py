# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        total = 0

        def traverse(grand, parent, child):
            nonlocal total
            if not child:
                return

            if grand and grand.val % 2 == 0:
                total += child.val

            traverse(parent, child, child.left)
            traverse(parent, child, child.right)
        traverse(None, None, root)

        return total