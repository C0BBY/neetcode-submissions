class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            char = s[i]
            temp = set(char)

            for j in range(i+1, len(s)):
                if s[j] not in temp:
                    temp.add(s[j])                                     
                else:
                    break
            count = max(count, len(temp))                                            
        return count