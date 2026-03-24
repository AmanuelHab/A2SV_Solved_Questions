# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def find(target):
            curr = root
            while curr and curr.val != target:
                if curr.val > target:
                    curr = curr.left
                else:
                    curr = curr.right
            if curr and curr.val == target:
                return True
            return False
        def traverse(node):
            if not node:
                return False
            target = k - node.val
            if target != node.val and find(target):
                return True
            return traverse(node.left) or traverse(node.right)
        return traverse(root)