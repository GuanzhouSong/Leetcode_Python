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
        matrix[i][j], matrix[size - 1 - j][size - 1 - i] = matrix[size - 1 - j][
                                                             size - 1 - i], \
                                                           matrix[i][j]
    return matrix

  def rotate180(self, matrix):
    size = len(matrix)
    for i in range(0, (size + 1) // 2):
      matrix[size - i - 1], matrix[i] = matrix[i], matrix[size - i - 1]
    return matrix

  def rotate2(self, matrix):
    for i in range(0, len(matrix)):
      for j in range(i + 1, len(matrix[i])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix[::-1]


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate2(matrix)
print(matrix)
