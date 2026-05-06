# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stk = deque([root]) if root else None

        # print(stk, stk.popleft().val)

        while stk:
            count = len(stk)
            temp = []
            while count:
                count-=1
                node = stk.popleft()
                temp.append(node.val)
                if node.left:
                    stk.append(node.left)
                if node.right:
                    stk.append(node.right)
            res.append(temp)
        
        return res            