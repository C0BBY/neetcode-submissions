class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def generate(op, cl, seq):
            if op == cl == n:
                res.append(seq)
                return

            if op < n:
                generate(op+1, cl, seq+"(")
            if cl < op:
                generate(op, cl+1, seq+")")
        
        generate(0,0,"")

        return res
