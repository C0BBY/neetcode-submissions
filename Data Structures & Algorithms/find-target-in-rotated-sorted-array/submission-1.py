class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > nums[-1]:
                l = mid+1
            else:
                r = mid-1
        print(l)

        r = len(nums)-1
        if target > nums[-1]:
            l, r = 0, l-1

        print(f"{l} {r}")
        while l<= r:
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid-1
            else:
                return mid                
        return -1