class Solution:
  def minCut(self, s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    cut = [i - 1 for i in range(n + 1)]
    for i in range(n):
      j = 0
      for j in range(min(i, n - i) + 1):
        while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
          cut[i + j + 1] = min(cut[i + j + 1], cut[i - j])
