class Solution:
  def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    res = []
    self.helper([], n, k, 1, res)
    return res

  def helper(self, temp, n, k, m, res):
    if k == 0:
      res.append(temp.copy())
    else:
      for i in range(m, n - k + 2):
        temp.append(i)
        self.helper(temp, n, k - 1, i + 1, res)
        temp.pop()


s = Solution()
print(s.combine(4, 2))
