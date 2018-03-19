class Solution:
  def partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    path, res = [], []
    self.helper(s, 0, path, res)
    return res

  def helper(self, s, pos, path, res):
    if pos == len(s):
      res.append(path.copy())
    else:
      for i in range(pos, len(s)):
        if self.isPal(s, pos, i):
          path.append(s[pos:i + 1])
          self.helper(s, i + 1, path, res)
          path.pop()

  def isPal(self, s, l, r):
    while l < r:
      if s[l] != s[r]:
        return False
      l += 1
      r -= 1
    return True


s = Solution()
print(s.partition("aab"))
