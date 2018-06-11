class Solution:
  def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
      return False
    else:
      a, b = dict(), dict()
      for i in range(len(s)):
        if a.get(s[i], -1) != b.get(t[i], -1):
          return False
        else:
          a[s[i]] = b[t[i]] = i
    return True


s = Solution()
print(s.isIsomorphic("paper", "title"))
