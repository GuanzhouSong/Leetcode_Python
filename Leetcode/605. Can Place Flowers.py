class Solution:
  def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    flowerbed = [0] + flowerbed + [0]
    available = 0
    for i in range(1, len(flowerbed) - 1, 1):
      if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
        flowerbed[i] = 1
        available += 1
    if available >= n:
      return True
    else:
      return False


s = Solution()
nums = [1, 0, 0, 0, 1, 0, 0]
print(s.canPlaceFlowers(nums, 2))
