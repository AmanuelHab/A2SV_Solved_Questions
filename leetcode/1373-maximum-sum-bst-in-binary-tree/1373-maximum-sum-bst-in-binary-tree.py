# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        sums = [0]
        def findBST(node):
            boolean = True
            sm = 0
            maxi = mini = node.val
            if node.left:
                b, s, mn, mx = findBST(node.left)
                sm += s
                mini = min(mn, mini)
                maxi = max(mx, maxi)
                boolean = boolean and b and node.val > mx
            if node.right:
                b, s, mn, mx = findBST(node.right)
                sm += s
                mini = min(mn, mini)
                maxi = max(mx, maxi)
                boolean = boolean and b and node.val < mn
            sm += node.val
            
            if boolean:
                sums.append(sm)
            return [boolean, sm, mini, maxi]
            
        findBST(root)
        print(sums)
        return max(sums)