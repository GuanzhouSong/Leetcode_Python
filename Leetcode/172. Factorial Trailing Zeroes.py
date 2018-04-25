class Solution:
  def trailingZeroes(self, n):
    """
    :type n: int
    :rtype: int
    """
    res = 0
    mul = 5
    while mul <= n:
      res += n // 5
      n = n // 5
    return res
