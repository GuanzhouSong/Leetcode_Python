class Solution:
  def restoreIpAddresses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    res = []
    self.helper("", s, 0, res)
    return res

  def helper(self, path, st, k, res):
    if k == 4 or len(st) == 0:
      if k == 4 and len(st) == 0:
        res.append(path[1:])
      return
    m = 1 if st[0] == "0" else 3
    i = 1
    while i <= min(m, len(st)):
      part = st[0:i]
      if int(part) <= 255:
        self.helper(path + "." + part, st[i:], k + 1, res)
      i += 1


s = Solution()
st = "010010"
print(s.restoreIpAddresses(st))
