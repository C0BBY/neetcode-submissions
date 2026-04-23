class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker = {}
        for c in s:
            checker[c] = checker.get(c, 0)+1      
        for c in t:
            if not checker.get(c):
                print(c)
                return False
            else:
                new_val = checker[c] - 1                                                        
                if new_val:
                    checker[c] = new_val
                else:
                    checker.pop(c)
        return False if checker  else True                   