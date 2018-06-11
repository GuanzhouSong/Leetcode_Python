class Solution:
  def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 1:
      return 1
    low, high = 0, x
    while low <= high:
      mid = (low + high) // 2
      if mid ** 2 <= x < (mid + 1) ** 2:
        return mid
      elif mid ** 2 > x:
        high = mid
      else:
        low = mid
    return None


s = Solution()
print(s.mySqrt(8))
