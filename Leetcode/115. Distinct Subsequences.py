class Solution:
  def numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    mem = [[1 for _ in range(len(s) + 1)]] + [[0 for _ in range(len(s) + 1)] for
                                              _
                                              in range(len(t))]
    for i in range(0, len(t)):
      for j in range(0, len(s)):
        if s[j] == t[i]:
          mem[i + 1][j + 1] = mem[i][j] + mem[i + 1][j]
        else:
          mem[i + 1][j + 1] = mem[i + 1][j]
    return mem[-1][-1]


s = Solution()
print(s.numDistinct("ddd", "dd"))
