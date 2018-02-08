class Solution:
  def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    s = "1"
    if n < 2:
      return s
    for _ in range(n - 1):
      p = 0
      temp = ""
      while p < len(s):
        t = s[p]
        count = 0
        while p < len(s) and s[p] == t:
          count += 1
          p += 1
        temp += str(count)
        temp += str(t)
      s = temp
    return s


s = Solution()
print(s.countAndSay(6))
