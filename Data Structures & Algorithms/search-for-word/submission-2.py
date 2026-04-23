class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()

        def dfs(y, x, i=0):
            if i >= len(word):
                return True
            if y<0 or x<0 or y>=len(board) or x>=len(board[0]):
                return False    
            if board[y][x] != word[i] or (y,x) in path:
                return False
            i+=1
            path.add((y,x))
            isValid = (
                dfs(y+1, x, i) or
                dfs(y-1, x, i) or
                dfs(y, x+1, i) or
                dfs(y, x-1, i)
            )
            path.remove((y,x))
            return isValid

        for y,_ in enumerate(board):
            for x, _ in enumerate(board[y]):
                if dfs(y, x):
                    return True
        return False                    