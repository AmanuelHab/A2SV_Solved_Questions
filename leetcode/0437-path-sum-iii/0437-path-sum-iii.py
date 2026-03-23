# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sum_count = defaultdict(int)
         
        def traverse(node, prefix_sum):
            if not node:
                return
            
            for i in range(len(prefix_sum)):
                prefix_sum[i] += node.val
            prefix_sum.append(node.val)

            for i in range(len(prefix_sum)):
                sum_count[prefix_sum[i]] += 1
            
            traverse(node.left, prefix_sum[:])
            traverse(node.right, prefix_sum[:])
        
        traverse(root, [])
        return sum_count[targetSum]