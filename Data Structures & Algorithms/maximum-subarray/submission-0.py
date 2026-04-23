class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        aggr = -float('inf')            
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr+=nums[j]
                aggr = max(aggr, curr)     
        return aggr