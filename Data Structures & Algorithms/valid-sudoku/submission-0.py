class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        row checkers, col checker, box checker
        focus on the numbers
        algo:
        if . skip, get the box index, check the value in row col box checker
        if dup, ret flase, else add to all three checker
        use set so using in will take O(1)
        """

        # each set for each row, col, box
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        # traverse the each cell
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    target = board[r][c]
                    # compute box index
                    b = (r // 3) * 3 + (c // 3)
                    if target in rows[r] or target in cols[c] or target in boxes[b]:
                        return False
                    else:
                        rows[r].add(target)
                        cols[c].add(target)
                        boxes[b].add(target)
        return True


