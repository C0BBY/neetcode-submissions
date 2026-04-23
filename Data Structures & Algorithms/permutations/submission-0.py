class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        container = set(nums)
        res = []

        def dfs(path):
            if len(path) >= len(nums):
                res.append(path[:])
                return                
            for x in container:
                if x not in path:
                    path.append(x)                    
                    dfs(path)
                    path.pop()

        dfs([])
        
        return res