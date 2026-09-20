# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        
        stack = [(root, 1)]
        best = 1

        while stack:
            node = stack.pop()
            if not (node[0].left or node[0].right):
                best = max(node[1], best)
            else:
                if node[0].left:
                    stack.append((node[0].left, node[1] + 1))
                if node[0].right:
                    stack.append((node[0].right, node[1] + 1))
        
        return best
