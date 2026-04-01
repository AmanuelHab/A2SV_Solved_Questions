# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(max(nums))
        def construct(node, arr):
            if not arr:
                return
            maxi = max(arr)
            node.val = maxi

            if len(arr) <= 1:
                return node

            i = arr.index(maxi)
            node.left = construct(TreeNode(), arr[:i])
            node.right = construct(TreeNode(), arr[i + 1:])
            return node
        root = construct(root, nums)
        return root