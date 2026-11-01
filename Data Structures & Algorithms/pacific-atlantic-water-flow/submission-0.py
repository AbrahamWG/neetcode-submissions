class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start from each border and work inwards, go neibor bigger equal to
        
        row, col = len(heights), len(heights[0])
        if row == 1 and col == 1:
            return [[0, 0]]
        
        ret = []
        seen = set()
        pacific = set()
        atlantic = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def helper(start, r, c, ocean):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            point = (r, c)
            if point in ocean:
                return
            if heights[r][c] < start:
                return
            ocean.add(point)
            if point not in seen and point in pacific and point in atlantic:
                ret.append([point[0], point[1]]) # needs a list, not tuple
                seen.add(point)
            for d in directions:
                helper(heights[r][c], r+d[0], c+d[1], ocean)
        
        # 4 loops from 2 oceans border
        for i in range(row):
            helper(heights[i][0], i, 0, pacific)
        for j in range(col):
            helper(heights[0][j], 0, j, pacific)
        for i in range(row):
            helper(heights[i][col-1], i, col-1, atlantic)
        for j in range(col):
            helper(heights[row-1][j], row-1, j, atlantic)

        return ret