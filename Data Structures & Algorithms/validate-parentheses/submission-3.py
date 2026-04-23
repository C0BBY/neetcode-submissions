class Solution:
    def isValid(self, s: str) -> bool:
        checker = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stk = []

        for ch in s: 
            if ch in checker:
                stk.append(ch)
            else:
                if stk and checker[stk[-1]] == ch:
                    stk.pop()
                else:
                    return False                
        return not stk
