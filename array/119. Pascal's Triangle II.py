class Solution:
  def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    rowIndex += 1
    if rowIndex is 0:
      return []
    res = [1]
    for i in range(1, rowIndex):
      temp1 = res + [0]
      temp2 = [0] + res
      res = [temp1[i] + temp2[i] for i in range(len(temp2))]
    return res


s = Solution()
print(s.getRow(3))
