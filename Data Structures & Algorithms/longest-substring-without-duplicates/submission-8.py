
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        count = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in store:
                l = r = store[s[r]] + 1
                store = {}
            store[s[r]] = r
            count = max(count, (r - l) + 1)
            print(s[l:r + 1])
            r += 1
        return count