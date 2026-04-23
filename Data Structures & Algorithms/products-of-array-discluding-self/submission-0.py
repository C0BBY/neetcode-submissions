class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        for i in range(len(nums)):
            if i==0:
                res.append(math.prod(nums[i+1:]))
            elif i == (len(nums)-1):
                res.append(math.prod(nums[:len(nums)-1]))                    
            else:
                res.append(math.prod(nums[:i]+nums[i+1:]))                                                
        return res