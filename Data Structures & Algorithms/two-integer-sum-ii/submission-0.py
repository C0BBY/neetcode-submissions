class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            temp = [i+1]
            seek =  target - numbers[i]
            
            for j in range(i+1, len(numbers)):
                if numbers[j] == seek:
                    temp.append(j+1)
                    return temp
        return []
    