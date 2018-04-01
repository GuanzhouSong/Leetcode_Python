class Solution:
  def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    if len(s) < 1:
      return res
    n = len(s)
    for i in range(n):
      res = res * 26 + int(ord(s[i]) - ord("A")) + 1
    return res


s = Solution()
print(s.titleToNumber("Z"))
