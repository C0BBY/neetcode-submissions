class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0]*(len(temperatures))
        for i, x in enumerate(temperatures):
            if stk:
                while stk and stk[-1][0] < x:
                    print(stk)
                    item, idx = stk.pop()
                    res[idx] = (i - idx) 
            
            stk.append((x, i))        
        return res                                    