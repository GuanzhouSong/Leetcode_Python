class Solution:
  def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    slow, fast = n, n
    slow = self.squareSum(slow)
    fast = self.squareSum(fast)
    fast = self.squareSum(fast)
    while slow != fast:
      slow = self.squareSum(slow)
      fast = self.squareSum(fast)
      fast = self.squareSum(fast)
    if slow == 1:
      return True
    else:
      return False

  def squareSum(self, n):
    sum = 0
    while n > 0:
      temp = n % 10
      sum += temp ** 2
      n //= 10
    return sum


s = Solution()
print(s.isHappy(19))
