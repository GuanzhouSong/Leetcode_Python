class Solution:
  def findPoisonedDuration(self, timeSeries, duration):
    """
    :type timeSeries: List[int]
    :type duration: int
    :rtype: int
    """
    total = duration * len(timeSeries)
    for i in range(1, len(timeSeries)):
      total -= max(0, duration - (timeSeries[i] - timeSeries[i - 1]))
    return total


s = Solution()
nums = [1, 4]

print(s.findPoisonedDuration(nums, 2))
