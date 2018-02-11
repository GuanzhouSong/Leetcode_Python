import math


class Solution:
  def getPermutation(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    nums = [i for i in range(1, n + 1)]
    res = ""
    k -= 1
    while n > 0:
      n -= 1
      index, k = divmod(k, math.factorial(n))
      res += str(nums[index])
      nums.remove(nums[index])
    return res


s = Solution()
print(s.getPermutation(3, 4))
