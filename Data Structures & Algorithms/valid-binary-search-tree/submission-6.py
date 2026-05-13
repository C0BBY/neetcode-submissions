# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(-float("inf"), float("inf"),root)
    
    def dfs(self, low, high, node) -> bool:
        if not node:
            return True

        if not low < node.val < high:
            return False

        return self.dfs(low, node.val, node.left) and self.dfs(node.val, high, node.right)             