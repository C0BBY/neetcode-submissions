# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.bfs(root,0)
        return self.res
                
    def bfs(self, root, level):
        if not root:
            return
        if level == len(self.res):
            self.res.append([])            
        self.res[level].append(root.val)
        level+=1
        self.bfs(root.left, level)
        self.bfs(root.right, level)
