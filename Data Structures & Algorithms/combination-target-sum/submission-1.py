class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(idx = 0):
            total = sum(path)
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return

            for i in range(idx, len(nums)):                
                path.append(nums[i])
                dfs(i)
                path.pop()
        dfs()

        return res                