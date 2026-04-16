# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answers = []
        def traverse(node):
            if not node:
                return 0
                
            left_val = traverse(node.left)
            right_val = traverse(node.right)

            ans = node.val + left_val + right_val
            # print(node.val)
            answers.append(node.val)
            # print(answers)
            if left_val:
                answers.append(left_val)
            answers.append(node.val + left_val)
            if right_val:
                answers.append(right_val)
            answers.append(node.val + right_val)
            answers.append(ans)

            return node.val + max(left_val, right_val, 0)
        traverse(root)
        return max(answers)