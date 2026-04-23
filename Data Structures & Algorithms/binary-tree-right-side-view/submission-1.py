# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root]) if root else None
        while queue:
            sz = len(queue)
            for i in range(sz):
                curr = queue.popleft()
                if i == (sz-1):
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:                    
                    queue.append(curr.right)
        
        return res                