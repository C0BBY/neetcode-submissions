class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        def dfs(y, x):
            if y < 0 or x < 0 or y == len(grid) or x == len(grid[y]):
                return 0
            if grid[y][x] != 1:
                return 0 
            grid[y][x] = 0
            return (dfs(y+1, x) + dfs(y-1, x) + dfs(y, x+1) + dfs(y, x-1))+1            
        
        maximum_land = 0
    
        for y,_ in enumerate(grid):
            for x, c in enumerate(grid[y]):
                if c:
                    maximum_land = max(maximum_land, dfs(y, x))
        
        return maximum_land