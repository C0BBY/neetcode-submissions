class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        container = set()
        for x in nums:
            if x in container:
                return x
            else:
                container.add(x)
        return 0                                