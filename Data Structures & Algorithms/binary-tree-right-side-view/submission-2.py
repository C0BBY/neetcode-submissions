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
            temp = []
            while right:
                right-=1
                curr = stk.popleft() 
                if curr:
                    temp.append(curr.val)
                    stk.append(curr.left)
                    stk.append(curr.right)
            if temp:
                res.append(temp[-1])
        return res

            
            