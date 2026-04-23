class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(idx):
            res.append(subset[:])
            if idx >= len(nums):
                return
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()

        dfs(0)
        
        return res                
        