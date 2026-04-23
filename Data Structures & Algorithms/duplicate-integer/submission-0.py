class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = set()
        for x in nums:
            if x in checker:
                return True 
            else:
                checker.add(x)                
        return False                