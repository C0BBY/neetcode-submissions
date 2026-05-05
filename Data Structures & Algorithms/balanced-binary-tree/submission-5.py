# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]
        
    def dfs(self, node):
        if not node:
            return 0, True
        left, lb = self.dfs(node.left) 
        right, rb = self.dfs(node.right)        
        return max(left, right)+1 , lb and rb and abs(left-right) <=1 
    
             