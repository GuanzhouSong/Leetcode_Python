class Solution:
  def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows is 0:
      return []
    res = [[1]]
    for i in range(1, numRows):
      temp1 = res[-1] + [0]
      temp2 = [0] + res[-1]
      res.append([temp1[i] + temp2[i] for i in range(len(temp2))])
    return res

s = Solution()
print(s.generate(10))
