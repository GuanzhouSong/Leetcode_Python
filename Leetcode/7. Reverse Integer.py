class Solution:
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    s = (x > 0) - (x < 0)
    r = int(str(s * x)[::-1])
    return s * r * (r < 2 ** 31)


s = Solution()
print(s.reverse(-123))
