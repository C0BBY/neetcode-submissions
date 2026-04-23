class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def dfs(idx, subset):            
            res.add(tuple(subset[:]))                
            if idx >= len(nums):
                return

            for i in range(idx, len(nums)):
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop()
        dfs(0, [])
        
        return [list(x) for x in res]