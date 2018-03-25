class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    res = [False for _ in range(len(s) + 1)]
    res[0] = True
    for i in range(0, len(s) + 1):
      for j in range(0, i):
        if res[j] and s[j:i] in wordDict:
          res[i] = True
    return res[-1]


s = "leetcode"
worddict = ["leet", "code"]
so = Solution()
print(so.wordBreak(s, worddict))
