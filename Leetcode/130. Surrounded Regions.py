class Solution:
  def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    row = len(board)
    if row < 1:
      return
    col = len(board[0])
    for i in range(row):
      self.change(board, i, 0, row, col)
      if col > 1:
        self.change(board, i, col - 1, row, col)
    for j in range(1, col - 1):
      self.change(board, 0, j, row, col)
      if row > 1:
        self.change(board, row - 1, j, row, col)
    for i in range(row):
      for j in range(col):
        if board[i][j] == 'O':
          board[i][j] = 'X'
    for i in range(row):
      for j in range(col):
        if board[i][j] == '1':
          board[i][j] = 'O'

  def change(self, board, i, j, row, col):
    if board[i][j] == 'O':
      board[i][j] = '1'
      if i > 1:
        self.change(board, i - 1, j, row, col)
      if j > 1:
        self.change(board, i, j - 1, row, col)
      if i < row - 1:
        self.change(board, i + 1, j, row, col)
      if j < col - 1:
        self.change(board, i, j + 1, row, col)
