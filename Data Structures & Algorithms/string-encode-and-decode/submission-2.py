class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for x in strs:
            encoded+=f"{len(x)}#{x}"
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            if s[i] == "#":
                count = int(s[:i])
                decoded.append(s[i+1:i+1+count])        
                s = s[i+1+count:]
                print(s)
                i = 0
            else:
                i+=1
        return decoded                        