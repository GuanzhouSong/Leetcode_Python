class Solution:
  def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    res = ""
    while n > 0:
      n -= 1
      res = chr(n % 26 + ord("A")) + res
      n = n // 26
    return res


s = Solution()
print(s.convertToTitle(52))
