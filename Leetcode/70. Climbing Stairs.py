class Solution:
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    dic = {1: 1, 2: 2}
    for i in range(3, n + 1):
      dic[i] = dic.get(i - 1, 0) + dic.get(i - 2, 0)
    return dic[n]


s = Solution()
print(s.climbStairs(5))
