class Solution:
  def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    fr = False
    fc = False
    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          if i == 0:
            fr = True;
          if j == 0:
            fc = True;
          matrix[0][j] = 0
          matrix[i][0] = 0

    for i in range(1, m):
      for j in range(1, n):
        if matrix[i][0] is 0 or matrix[0][j] is 0:
          matrix[i][j] = 0

    if fr:
      matrix[0][:] = [0 for i in range(len(matrix[0]))]

    if fc:
      for i in range(0, len(matrix)):
        matrix[i][0] = 0


s = Solution()
feedin = [
  [0, 2, 3],
  [5, 0, 8],
  [1, 8, 4]
]
s.setZeroes(feedin)
print(feedin)
