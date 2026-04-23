class Solution:
    def isValid(self, s: str) -> bool:
        matcher = {
            "(":")",
            "[":"]",
            "{":"}",
        }

        stk = []

        for c in s:
            if c in matcher:
                stk.append(c)
            else:
                if stk and matcher[stk[-1]] == c:
                    stk.pop()
                else:
                    return False                    

        return not stk
