# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stk = [root]
        while stk:
            node = stk.pop()        
            if node:
                node.left, node.right = node.right, node.left                                
                stk.extend([node.left,node.right])
             
        return root            
        
