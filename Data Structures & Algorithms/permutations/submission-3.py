class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        container = set(nums)
        res = []
        checker = set()
        def dfs(path):
            if len(path) >= len(nums):
                res.append(path)
                return                
            for x in container:
                if x not in path:
                    checker.add(x)
                    dfs(path+[x])
                    checker.remove(x)

        dfs([])
        return res