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
        min(triangle[index][i] + record[i - 1], triangle[index][i] + record[i]))
    temp.append(triangle[index][-1] + record[-1])
    return temp


s = Solution()
t = [
  [2],
  [3, 4],
  [6, 5, 7],
  [4, 1, 8, 3]
]
print(s.minimumTotal(t))
