class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        path = set()
        res = 0
        
        while l <= r < len(s):
            if s[r] in path:
                while l < r and s[r] in path:
                    path.remove(s[l])
                    l+=1
            
            seq = s[l:r+1]
            res = max(res, len(seq))
            path.add(s[r])                
            r+=1

        return res


