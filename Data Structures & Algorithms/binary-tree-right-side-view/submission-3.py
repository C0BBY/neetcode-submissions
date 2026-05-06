# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = deque([root])

        while stk:
            right = len(stk)
            last = None 
            while right:
                right-=1
                curr = stk.popleft()
                if curr:
                    stk.append(curr.left)
                    stk.append(curr.right)
                    last = curr.val
            if last:
                res.append(last)
        return res

            
            