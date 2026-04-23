class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        checker = set()
        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return                
            for x in nums:
                if x not in checker:
                    checker.add(x)
                    path.append(x)
                    dfs(path)
                    path.pop()
                    checker.remove(x)

        dfs([])
        return res