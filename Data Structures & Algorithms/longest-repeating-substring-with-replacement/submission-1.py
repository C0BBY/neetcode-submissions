class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        count = 0

        while r<len(s):
            charmap = defaultdict(int)
            sub = s[l:r+1]

            for x in sub:
                charmap[x]+=1
            
            max_chars = sorted(charmap.items(), key= lambda item : item[1])[-1][-1]
            print(max_chars)
            if (len(sub)- max_chars) > k:
                l+=1
            else:
                count= max(count, len(sub))
                r+=1
        return count