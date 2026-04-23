class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l = 0
        store = set()

        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            store.add(s[r])                
            count = max(count, (r-l)+1)
        return count
           
