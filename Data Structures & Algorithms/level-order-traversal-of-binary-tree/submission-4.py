# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stk = deque([root])

        while stk:
            count = len(stk)
            temp = []
            while count:
                count-=1
                node = stk.popleft()
                if node:
                    temp.append(node.val)
                    stk.append(node.left)
                    stk.append(node.right)
            if temp:
                res.append(temp)
        
        return res            