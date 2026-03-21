# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isTheSame(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val == node2.val:
                return isTheSame(node1.left, node2.left) and isTheSame(node1.right, node2.right)
        # Inorder traversal
        def traverse(node):
            if not node:
                return False
            if node.val == subRoot.val: 
                return isTheSame(node, subRoot) or traverse(node.left) or traverse(node.right)
            return traverse(node.left) or traverse(node.right)
        return traverse(root)