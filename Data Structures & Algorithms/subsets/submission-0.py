class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def dfs(idx):
            if idx>=len(nums):
                res.append(temp[:])                    
                return 
            temp.append(nums[idx])
            dfs(idx+1)
            
            temp.pop()
            dfs(idx+1)
        dfs(0)
        return res            

