# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, level):
            nonlocal res
            if not node:
                res = max(level, res)
                return
            level+=1
            dfs(node.left, level)            
            dfs(node.right, level)                

        dfs(root, 0)
        return res