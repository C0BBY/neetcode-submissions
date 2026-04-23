# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        curr = root
        res = []
        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left

            curr = stk.pop()            
            if not k-1:
                return curr.val
            else:
                k-=1
            # res.append(curr.val)
            curr = curr.right        
        return 0                                                        