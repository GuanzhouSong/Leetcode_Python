class Solution:
  def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    for i in range(len(board)):
      for j in range(len(board[0])):
        if self.helper(board, word, i, j, 0):
          return True
    return False

  def helper(self, board, word, x, y, i):
    if i == len(word):
      return True
    elif x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
      return False
    elif word[i] != board[x][y]:
      return False
    else:
      board[x][y] = "*"
      res = self.helper(board, word, x, y + 1, i + 1) or self.helper(board,
                                                                     word, x,
                                                                     y - 1,
                                                                     i + 1) or self.helper(
          board, word, x - 1, y, i + 1) or self.helper(board, word, x + 1, y,
                                                       i + 1)
      board[x][y] = word[i]
    return res


s = Solution()
board = [["A"]]
word = "AB"
print(s.exist(board, word))
