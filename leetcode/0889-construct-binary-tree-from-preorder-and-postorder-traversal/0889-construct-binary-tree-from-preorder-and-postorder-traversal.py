# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = None
        def build(parent, preord, postord):
            nonlocal root
            if not preord or not postord:
                return 
            if preord[0] == postord[-1]:
                node = TreeNode(preord[0])
                if not parent:
                    root = node
                else:
                    parent.left = node
                build(node, preord[1:], postord[:-1])
            else:
                l = TreeNode(preord[0])
                r = TreeNode(postord[-1])
                parent.left = l
                parent.right = r

                # Compute the next traversal orders
                l_ind = postord.index(preord[0])
                r_ind = preord.index(postord[-1])

                # Store the subtree preorder traversals
                left_subtree_preord = preord[1: r_ind]
                right_subtree_preord = preord[r_ind + 1:]

                # Store the subtree postorder traversals
                left_subtree_postord = postord[:l_ind]
                right_subtree_postord = postord[l_ind + 1:-1]
                
                build(l, left_subtree_preord, left_subtree_postord)
                build(r, right_subtree_preord, right_subtree_postord)
        build(root, preorder, postorder)
        return root