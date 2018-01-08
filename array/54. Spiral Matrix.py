class Solution:
  def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    res = []
    if len(matrix) == 0:
      return res
    rowBegin = 0
    rowEnd = len(matrix) - 1
    colBegin = 0
    colEnd = len(matrix[0]) - 1

    while rowBegin <= rowEnd and colBegin <= colEnd:
      for i in range(colBegin, colEnd + 1):
        res.append(matrix[rowBegin][i])
      rowBegin += 1

      for i in range(rowBegin, rowEnd + 1):
        res.append(matrix[i][colEnd])
      colEnd -= 1

      if rowBegin <= rowEnd:
        i = colEnd
        while i >= colBegin:
          res.append(matrix[rowEnd][i])
          i -= 1
      rowEnd -= 1

      if colBegin <= colEnd:
        i = rowEnd
        while i >= rowBegin:
          res.append(matrix[i][colBegin])
          i -= 1
      colBegin += 1

    return res

nums = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
solution = Solution()
print(solution.spiralOrder(nums))