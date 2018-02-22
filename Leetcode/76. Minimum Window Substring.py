import sys


class Solution:
  def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(s) <= 0 or len(t) <= 0:
      return ""
    dic = dict()
    for c in t:
      dic[c] = dic.get(c, 0) + 1
    start, end = 0, 0
    counter = len(t)
    minstart, minlength = 0, sys.maxsize
    while end < len(s):
      if dic.get(s[end], 0) > 0:
        counter -= 1
      dic[s[end]] = dic.get(s[end], 0) - 1
      end += 1
      while counter == 0:
        if end - start < minlength:
          minlength = end - start
          minstart = start
        dic[s[start]] = dic.get(s[start], 0) + 1
        if dic.get(s[start], 0) > 0:
          counter += 1
        start += 1
    return s[minstart:minstart + minlength] if minlength < sys.maxsize else ""


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
