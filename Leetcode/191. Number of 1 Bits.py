class Solution(object):
  def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    res = 0
    while n != 0:
      res = res + (n & 1)
      n = n >> 1
    return res


s = Solution()
n = 1011000000001
print(s.hammingWeight(n))
