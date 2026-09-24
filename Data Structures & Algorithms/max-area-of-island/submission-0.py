class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sizes = [0]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            
            if grid[i][j] == 1:
                grid[i][j] = 0
                return (1 + 
                    dfs(i-1, j) + 
                    dfs(i+1, j) + 
                    dfs(i, j-1) + 
                    dfs(i, j+1)
                )
            else: 
                return 0
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sizes.append(dfs(i, j))

        return max(sizes)