class Solution:
    def isValid(self, s: str) -> bool:
        checker = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stk = []

        for i,ch in enumerate(s): 
            if ch in checker:
                stk.append(ch)
            else:
                if stk and checker[stk[-1]] == ch:
                    stk.pop()
                else:
                    return False                
        return not stk
