class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        store = set()

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            target = 0 - nums[i] 
            print(nums)
            while left < right:
                print((nums[i],nums[left], nums[right]))
                if (nums[left]+nums[right]) > target :
                    right-=1
                elif nums[left]+nums[right] < target:
                    left+=1
                else:
                    store.add((nums[i], nums[left], nums[right]))
                    right-=1
                    left+=1
        return [list(x) for x in store]                    