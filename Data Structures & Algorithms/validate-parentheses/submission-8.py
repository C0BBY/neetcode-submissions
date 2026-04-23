class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapper = {
            '(':')',
            '{':'}',
            '[':']',
        }
        for char in s:
            if char in mapper:
                stk.append(char)
            elif not stk:
                return False
            else:
                curr = stk.pop()
                if mapper[curr] != char:
                    return False
        return not stk                    

