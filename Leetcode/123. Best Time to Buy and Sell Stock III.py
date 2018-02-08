import sys


class Solution:
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) is 0:
      return 0
    firstbuy = sys.maxsize
    firstSell = 0
    secondbuy = -1 * sys.maxsize
    secondsell = 0
    for curPrice in prices:
      firstbuy = min(firstbuy, curPrice)
      firstSell = max(firstSell, curPrice - firstbuy)
      secondbuy = max(secondbuy, firstSell - curPrice)
      secondsell = max(secondsell, curPrice + secondbuy)
    return secondsell


s = Solution()
prices = [7, 1, 5, 3, 8, 4]
print(s.maxProfit(prices))
