class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        count = 0
        
        for num in store:
            temp = 0
            curr = num
            if (num-1) not in store:
                while curr in store:
                    temp+=1
                    curr+=1
                count = max(temp, count)                    
        
        return count                