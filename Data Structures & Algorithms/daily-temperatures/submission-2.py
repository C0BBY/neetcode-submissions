class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0]*len(temp)

        for i in range(len(temp)):
            counter = 0
            for j in range(i+1, len(temp)):
                counter+=1
                if temp[j]>temp[i]:
                    res[i] = counter
                    break                    
        return res                    