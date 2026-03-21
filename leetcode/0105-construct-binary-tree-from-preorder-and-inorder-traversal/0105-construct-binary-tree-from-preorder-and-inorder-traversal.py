# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = None
        def traverse(parent, dir, preord, inord):
            nonlocal root
            if not preord:
                return
            par_ind = inord.index(preord[0])
            left_inord = inord[:par_ind]
            right_inord = inord[par_ind + 1:]

            left_preord = preord[1:len(left_inord) + 1]
            right_preord = preord[len(left_inord) + 1:]

            node = TreeNode(preord[0])
            if not root:
                root = node
            if dir == 'l':
                parent.left = node
            if dir == 'r':
                parent.right = node
                
            traverse(node, 'l', left_preord, left_inord)
            traverse(node, 'r', right_preord, right_inord)

        traverse(root, None, preorder, inorder)
        return root