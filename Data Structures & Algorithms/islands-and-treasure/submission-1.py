from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # traverse grid once to mark all treasure chest
        # append all to deque
        # use BFS to update neighbors distance at a time
        
        r, c = len(grid), len(grid[0])

        queue = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            row, col = queue.popleft()
            for d in directions:
                nr = row + d[0]
                nc = col + d[1]
                if nr < 0 or nr >= r or nc < 0 or nc >= c:
                    continue
                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))
                    