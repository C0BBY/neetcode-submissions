class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        count = 0
        l = 0

        for r in range(len(s)):
            ch = s[r]
            if ch in store:
                l = max(l, store[ch]+1)
            store[ch] = r
            count = max(count, (r-l)+1)
        
        return count