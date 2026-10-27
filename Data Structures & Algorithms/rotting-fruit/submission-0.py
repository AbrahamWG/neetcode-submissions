class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # trace every rotten oranges in the whole grid at time 0
        # update the grid simultaneously at each increment of time
        # BFS:
            # mark all rotten oranges at the beginning
            # put in queue all the rotten
            # check all nei of rotten
            # update time after queue done for first phase rotten

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        # loop the whole grid, find all rotten and count how many fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minutes = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = r+dr, c+dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        queue.append((new_r, new_c))
            minutes += 1
        return minutes if fresh == 0 else -1

        # queue = deque()
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 2:
        #             queue.append((i, j))

        # def check(x, y):
        #     if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        #         return False
        #     if grid[x][y] == 1:
        #         grid[x][y] = 2
        #         return True
        #     else:
        #         return False
            
        # time = 0
        # num_oranges_per_time = len(queue)
        # while queue:
        #     if num_oranges_per_time == 0:
        #         time += 1
        #         num_oranges_per_time = len(queue)
        #     directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        #     # process rotten
        #     rotting = queue.popleft()
        #     for di in directions:
        #         x, y = rotting[0], rotting[1]
        #         if check(x+di[0], y+di[1]):
        #             queue.append((x+di[0], y+di[1]))
        #     num_oranges_per_time -= 1
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             return -1
        # return time