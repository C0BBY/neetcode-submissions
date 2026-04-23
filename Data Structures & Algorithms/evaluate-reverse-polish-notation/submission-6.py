class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        delim = set(['+', '-', '*', '/'])
        res = 0

        for ch in tokens:                                                                                   
            if ch in delim and stk:    
                temp = 0
                suf = int(stk.pop())
                pre = int(stk.pop())
                if ch == '+':
                    temp=pre+suf                      
                if ch == '-':
                    temp=pre-suf
                if ch == '*':
                    temp=pre*suf
                if ch == '/':
                    temp=int(pre/suf)
                stk.append(temp)
                res = temp
            else:
                stk.append(ch)
    
        return int(stk.pop())          