class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = count =  0
        while r < len(s):
            cmap  = {}
            sub = s[l: r+1]
            for x in sub:
                cmap[x] = cmap.get(x, 0)+1
            max_count = cmap[max(cmap, key=cmap.get)]
            if (len(sub)-max_count) <= k:
                count = max(len(sub), count)
                r+=1                
            else:
                l+=1                
        return count

