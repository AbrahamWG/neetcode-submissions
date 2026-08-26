class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row index
        top, bot =  0, len(matrix) - 1

        # col index
        l, r = 0, len(matrix[0]) - 1

        # solve the row first
        while top <= bot:
            mid = (top + bot) // 2
            # reduce to left window
            if target < matrix[mid][l]:
                bot = mid - 1
            # reduce to right window
            elif target > matrix[mid][r]:
                top = mid + 1
            else:
                break

        # solve the col, when top == bot
        while l <= r:
            m = (l + r) // 2
            # break here
            if matrix[mid][m] == target:
                return True
            elif matrix[mid][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False