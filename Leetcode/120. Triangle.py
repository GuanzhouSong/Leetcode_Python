class Solution:
  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    minium = 99999
    record = triangle[0]
    for i in range(1, len(triangle)):
      record = self.help(record, i, triangle)
    return min(record)

  def help(self, record, index, triangle):
    temp = []
    size = len(triangle[index])
    temp.append(triangle[index][0] + record[0])
    for i in range(1, size - 1):
      temp.append(
          min(triangle[index][i] + record[i - 1],
              triangle[index][i] + record[i]))
    temp.append(triangle[index][-1] + record[-1])
    return temp

  def minimumTotalv2(self, triangle):
    self.helpv2(1, 0, triangle)
    print(triangle)
    self.helpv2(1, 1, triangle)
    print(triangle)
    return min(triangle[-1])

  def helpv2(self, row, index, triangle):
    if row >= len(triangle):
      return
    if index is 0:
      triangle[row][0] = triangle[row - 1][0] + triangle[row][0]
    elif index is len(triangle[row]) - 1:
      triangle[row][-1] = triangle[row - 1][-1] + triangle[row][-1]
    else:
      triangle[row][index] = min(
          triangle[row][index] + triangle[row - 1][index],
          triangle[row][index] + triangle[row - 1][index - 1])
    for i in range(len(triangle[row])):
      self.helpv2(row + 1, i, triangle)


s = Solution()
t = [
  [2],
  [3, 4],
  [6, 5, 7],
  [4, 1, 8, 3]
]
print(s.minimumTotal(t))
