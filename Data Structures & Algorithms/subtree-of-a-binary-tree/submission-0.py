# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def isSameTree(node, subnode):
            if not node and not subnode:
                return True
            if node and subnode and node.val == subnode.val:
                return isSameTree(node.left, subnode.left) and isSameTree(node.right, subnode.right)
            else:
                return False
                
        stk = [root]

        while stk:
            node = stk.pop()
            if node:
                if node.val == subroot.val:
                    if isSameTree(node, subroot):
                        return True
                stk.append(node.left)
                stk.append(node.right)
        
        return False











