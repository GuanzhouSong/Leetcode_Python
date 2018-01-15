class Solution:
  def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    matrix = self.rotate_45(matrix)
    matrix = self.rotate180(matrix)
    return matrix

  def rotate_45(self, matrix):
    size = len(matrix)
    for i in range(0, len(matrix)):
      for j in range(0, len(matrix[0]) - i):
        temp = matrix[i][j]
        matrix[i][j] = matrix[size - 1 - j][size - 1 - i]
        matrix[size - 1 - j][size - 1 - i] = temp
    return matrix

  def rotate180(self, matrix):
    size = len(matrix)
    for i in range(0, (size + 1) // 2):
      temp = matrix[size - i - 1]
      matrix[size - i - 1] = matrix[i]
      matrix[i] = temp
    return matrix


solution = Solution()
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(solution.rotate(matrix))
