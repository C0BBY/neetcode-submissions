class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        checker = {}
        for c in s:
            checker[c] = checker.get(c, 0)+1      
        for c in t:
            if c not in checker:
                return False
            else:
                checker[c] -= 1                                                        
                if not checker[c]:
                    checker.pop(c)
        return not checker