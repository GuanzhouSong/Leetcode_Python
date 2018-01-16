class Solution:
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
      return 0
    maximum = 0
    minimum = prices[0]
    for i in range(len(prices)):
      if prices[i] < minimum:
        minimum = prices[i]
      else:
        maximum = max(maximum, prices[i] - minimum)
    return maximum


s = Solution()
prices = [7, 1, 5, 3, 8, 4]
print(s.maxProfit(prices))
