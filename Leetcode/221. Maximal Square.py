class Solution:
  def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if len(matrix) == 0:
      return 0
    m, n = len(matrix), len(matrix[0])
    res = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    result = 0
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if matrix[i - 1][j - 1] == '1':
          res[i][j] = min(min(res[i - 1][j], res[i][j - 1]), res[i - 1][j - 1])
          result = max(result, res[i][j])
    return result ** 2
