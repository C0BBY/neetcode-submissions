class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        count = 0
        for num in store:
            pre = num - 1
            temp = 0                     
            
            while pre not in store and num in store:
                num +=1
                temp +=1

            count = max(count, temp)
        return count            