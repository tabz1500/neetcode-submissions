# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ancestor = None
        def common(root, p, q):
            if root == None:
                return False

            if root in (p,q):
                return root
        
            else:
                left = common(root.left, p, q)
                right = common(root.right, p, q)

                if left and right:
                    return root
                if left:
                    return left
                else:
                    return right

        return common(root, p, q)
