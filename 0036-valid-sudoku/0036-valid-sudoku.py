class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def areRowsValid():
            for row in board:
                nums = list(filter(str.isdigit, row))
                if len(nums) != len(set(nums)):
                    return False
            return True

        def areColumnsValid():
            for column in zip(*board):
                nums = list(filter(str.isdigit, column))
                if len(nums) != len(set(nums)):
                    return False
            return True

        def areSquaresValid():
            for i in range(0, 7, 3):
                for j in range(0, 7, 3):
                    square = [board[n][m] for n in range(i, i+3) for m in range(j, j+3)]
                    nums = list(filter(str.isdigit, square))
                    if len(nums) != len(set(nums)):
                        return False
            return True

        return areRowsValid() and areColumnsValid() and areSquaresValid()