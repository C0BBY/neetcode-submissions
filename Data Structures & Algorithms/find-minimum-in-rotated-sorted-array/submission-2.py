class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = len(nums)-1
        l, r = 0, last        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[last]:
                l = mid+1
            else:
                r = mid-1
        return nums[l]