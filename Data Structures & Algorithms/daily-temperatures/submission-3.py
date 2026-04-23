class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0]*len(temp)
        stk = []

        for i in range(len(temp)):
            while stk and stk[-1][1] < temp[i]:
                idx = stk.pop()[0]
                res[idx] = i-idx
            stk.append((i, temp[i]))
        return res                    