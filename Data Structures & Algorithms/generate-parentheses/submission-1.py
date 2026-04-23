class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr="", open=0, close=0):
            if close == n:
                res.append(curr)
                return 

            if open < n:
                dfs(curr+"(", open+1, close)    
            if close < open:
                dfs(curr+")",open, close+1)                                
        dfs()
        
        return res