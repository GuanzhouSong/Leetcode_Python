class Solution:
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    imax = 0
    l, r = 0, len(height) - 1
    while l < r:
      imax = max(imax, min(height[l], height[r]) * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
    return imax


s = Solution()
height = [6, 1, 2, 5, 4, 3]
print(s.maxArea(height))
