class Solution:
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs == None or len(strs) == 0:
      return "";
    pre = strs[0]
    for istr in strs:
      while istr.find(pre) != 0:
        pre = pre[:-1]
    return pre


s = Solution()
strs = ["abc", "abfg", "aoe", "abuy"]
print(s.longestCommonPrefix(strs))
