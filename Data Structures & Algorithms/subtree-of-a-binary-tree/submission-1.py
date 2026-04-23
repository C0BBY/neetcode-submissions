# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stk = [root]

        def isSameTree(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            if x.val != y.val:
                return False
            return isSameTree(x.left, y.left) and isSameTree(x.right, y.right)

        while stk:
            curr = stk.pop()
            if not curr:
                continue
            if curr.val == subRoot.val:
                if isSameTree(curr, subRoot):
                    return True
            stk.append(curr.left)            
            stk.append(curr.right)            

        return False