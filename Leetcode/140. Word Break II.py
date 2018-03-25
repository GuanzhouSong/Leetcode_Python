class Solution():
  dic = dict()

  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    res = []
    if not s or len(s) < 1:
      return res
    if s in self.dic:
      return self.dic.get(s, [])
    if s in wordDict:
      res.append(s)
    for i in range(1, len(s)):
      t = s[i:]
      if t in wordDict:
        temp = self.wordBreak(s[0:i], wordDict)
        if len(temp) > 0:
          for re in temp:
            res.append(re + " " + t)
    self.dic[s] = res
    return res


s = "a"
di = ["a"]
so = Solution()
print(so.wordBreak(s, di))
