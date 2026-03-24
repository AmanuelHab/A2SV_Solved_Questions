# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # A child can give/take to/from parent
        op = 0
        def postorder(parent, node): # To give priority to the children
            nonlocal op

            if node.left:
                postorder(node, node.left)
            if node.right:
                postorder(node, node.right)
            if parent:
                parent.val -= 1 - node.val
            op += abs(1 - node.val)

        postorder(None, root)
        return op