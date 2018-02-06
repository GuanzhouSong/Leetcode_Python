class Solution:
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for i in range(0, 9):
      row, col, cube = dict(), dict(), dict()
      for j in range(0, 9):
        if board[i][j] != '.' and board[i][j] in row.keys():
          return False
        row[board[i][j]] = 0
        if board[j][i] != '.' and board[j][i] in col.keys():
          return False
        col[board[j][i]] = 0
        rowindex = 3 * (i // 3)
        colindex = 3 * (i % 3)
        if board[rowindex + j // 3][colindex + j % 3] != '.' and \
            board[rowindex + j // 3][colindex + j % 3] in cube.keys():
          return False
        cube[board[rowindex + j // 3][colindex + j % 3]] = 0
    return True


s = Solution()
board = [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
         ["2", ".", ".", ".", ".", ".", ".", ".", "."],
         ["3", ".", ".", ".", ".", ".", ".", ".", "."],
         ["4", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", ".", "."],
         ["6", ".", ".", ".", ".", ".", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         ["8", ".", ".", ".", ".", ".", ".", ".", "."],
         ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
print(s.isValidSudoku(board))
