class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(numbers)):
            diff = target - numbers[i] 
            if hm.get(diff, 0):
                return [hm[diff], i+1]
            hm[numbers[i]] = i+1
        return []
    