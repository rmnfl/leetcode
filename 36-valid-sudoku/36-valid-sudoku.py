class Solution(object):
    def isValidSudoku(self, board):
        return (self.isSquaresValid(board) and 
                self.isHorizontalLinesValid(board) and 
                self.isVerticalLinesValid(board))  
    
    
    def isHorizontalLinesValid(self, board):
        for i in board:
            line = [n for n in i if n != '.']
            if len(line) != len(set(line)):
                return False
        return True
    
    
    def isVerticalLinesValid(self, board):
        for i in zip(*board):
            line = [n for n in i if n != '.']
            if len(line) != len(set(line)):
                return False
        return True
    
    
    def isSquaresValid(self, board):
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                square = [board[m][n] for m in range(i, i+3) for n in range(j, j+3) if board[m][n] != '.']
                if len(square) != len(set(square)):
                    return False
        return True
