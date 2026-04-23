class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:
            res+=(f"{len(str)}#{str}")
        return res            

    def decode(self, s: str) -> List[str]:
        res = []
        i= ptr = 0
        while i < len(s):
            if s[i] == '#':
                print(i)
                count = int(s[ptr:i])
                next = i+count+1
                res.append(s[i+1:next])
                ptr = i = next 
                continue
            i+=1
        return res            
