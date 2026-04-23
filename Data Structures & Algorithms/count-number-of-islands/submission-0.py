class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(y, x):
            
            if y < 0 or x < 0 or y == len(grid) or x == len(grid[y]):
                return
            if grid[y][x] != "1":
                return
            grid[y][x] = "#"
            dfs(y+1, x) or dfs(y-1, x) or dfs(y, x+1) or dfs(y, x-1)            

        counter = 0

        for y,_ in enumerate(grid):
            for x, c in enumerate(grid[y]):
                if c == "1":
                    counter+=1
                    dfs(y, x)
        
        return counter                    