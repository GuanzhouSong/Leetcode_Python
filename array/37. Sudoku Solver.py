class Solution:
  def solveSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if board is None or len(board) < 1:
      return
    self.board = board
    self.solve()
    print(board)

  def solve(self):
    for i in range(0, 9):
      for j in range(0, 9):
        if board[i][j] == '.':
          for n in range(1, 10):
            if self.isValid(i, j, n):
              board[i][j] = str(n)
              if self.solve():
                return True
              else:
                board[i][j] = '.'
          return False
    return True

  def isValid(self, row, col, n):
    for i in range(0, 9):
      if board[row][i] != '.' and board[row][i] == str(n):
        return False
      if board[i][col] != '.' and board[i][col] == str(n):
        return False
      if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and \
          board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == str(n):
        return False
    return True


s = Solution()
board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]
s.solveSudoku(board)
