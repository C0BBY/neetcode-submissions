class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1        
        while nums[l] > nums[r]:
            l+=1
        return nums[l]