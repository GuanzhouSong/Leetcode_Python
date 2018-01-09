class Solution:
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # search row
    if len(matrix) == 0 or len(matrix[0]) == 0:
      return False
    s, e = 0, len(matrix) - 1
    current = 0
    while s <= e:
      current = (s + e) // 2
      if matrix[current][0] <= target:
        if current != len(matrix) - 1:
          if matrix[current + 1][0] > target:
            break
          else:
            s = current + 1
        else:
          break
      else:
        e = current - 1

    rowindex = current
    current = 0

    s, e = 0, len(matrix[0]) - 1
    while s <= e:
      current = (s + e) // 2
      if matrix[rowindex][current] == target:
        return True
      if matrix[rowindex][current] < target:
        s = current + 1
      else:
        e = current - 1
    return False

  def searchMatrixv2(self, matrix, target):
    l = []
    for i in matrix:
      l = l + i
    s, e = 0, len(l) - 1
    while s <= e:
      current = (s + e) // 2
      if l[current] == target:
        return True
      if l[current] < target:
        s = current + 1
      else:
        e = current - 1
    return False


s = Solution()
feedin = [[-10], [-7], [-5]]
print(s.searchMatrixv2(feedin, -10))
