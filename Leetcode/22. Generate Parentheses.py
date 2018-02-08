class Solution:
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    self.helper('', n, n, res)
    return res

  def helper(self, p, left, right, res):
    if left:
      self.helper(p + '(', left - 1, right, res)
    if right > left:
      self.helper(p + ')', left, right - 1, res)
    if not right:
      res.append(p)


s = Solution()
print(s.generateParenthesis(3))
