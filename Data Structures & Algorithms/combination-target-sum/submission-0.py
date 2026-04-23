class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path=[], idx = 0):
            total = sum(path)
            if total > target:
                return
            if total == target:
                res.append(path)
                return

            for i in range(idx, len(nums)):                
                dfs(path+[nums[i]], i)
        dfs()

        return res                