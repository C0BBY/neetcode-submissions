# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, large):
            if not node:
                return
            dfs(node.left, max(large, node.val))
            dfs(node.right, max(large, node.val))
            
            if node.val >= large:
                self.count+=1

        dfs(root, root.val)
        
        return self.count            