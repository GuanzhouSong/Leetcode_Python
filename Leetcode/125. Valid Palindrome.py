class Solution:
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) < 1:
      return True
    l = []
    for c in list(s):
      if c.isalnum():
        l.append(c.lower())
    length = len(l)
    if length // 2 == length / 2:
      left = l[:length // 2]
      right = l[length // 2:]
    else:
      left = l[:length // 2]
      right = l[length // 2 + 1:]
    right.reverse()
    return left == right


s = Solution()
print(s.isPalindrome("aA"))
