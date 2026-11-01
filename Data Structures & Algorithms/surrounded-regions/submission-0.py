from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # BFS, start from the border go inwards
        # append cells to safe set() 
        # check out of border and if all adjacent nei are safe, stop search
        # final grid update
        # return None, final grid modified in place

        rows, cols = len(board), len(board[0])
        # check 1x1 grid
        if rows == 1 and cols == 1:
            return 

        queue = deque()
        safe = set()
        # fill in border cells to queue
        for r in range(rows):
            queue.append((r, 0))
            queue.append((r, cols-1))
        for c in range(cols):
            queue.append((0, c))
            queue.append((rows-1, c))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
        while queue:
            row, col = queue.popleft()
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if ((new_row, new_col) not in safe 
                and board[row][col] == "O" 
                and (0 <= new_row < rows and 0 <= new_col < cols)):
                    queue.append((new_row, new_col))
                    safe.add((new_row, new_col))
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if (r, c) not in safe and board[r][c] == "O":
                    board[r][c] = "X"
