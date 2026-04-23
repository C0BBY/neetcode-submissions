class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        count = 0
        l = 0
        for r in range(len(s)):
            ch = s[r]
            while ch in store:
                store.remove(s[l])
                l+=1
            store.add(ch)
            count = max(count, (r-l)+1)
        return count