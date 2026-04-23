class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk =[]
        delim = set(['+', '-', '*', '/'])
        for x in tokens:
            temp = 0
            if x in delim and stk:
                suf = stk.pop()
                pref = stk.pop()
                if x == '+':
                    temp = pref+suf                        
                if x == '-':
                    temp = pref-suf                    
                if x == '*':
                    temp = pref*suf
                if x == '/':
                    temp = int(pref/suf)
                stk.append(temp)
            else:
                stk.append(int(x))                
        return stk.pop()