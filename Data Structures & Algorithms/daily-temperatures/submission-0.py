class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = []            
        for i in range(len(temp)):
            diff = 0
            for j in range(i+1, len(temp)):
                if temp[i]< temp[j]:
                    diff = j-i
                    break
            res.append(diff)
        return res
