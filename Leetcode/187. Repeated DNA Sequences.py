class Solution:
  def findRepeatedDnaSequences(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    dic = dict()
    res = []
    for i in range(len(s) - 9):
      r = dic.get(s[i:i + 10], 0)
      if r != 0:
        dic[s[i:i + 10]] += 1
      else:
        dic[s[i:i + 10]] = 1
    return [i[0] for i in dic.items() if i[1] > 1]


so = Solution()
s = "AAAAAAAAAAAAAAB"
print(so.findRepeatedDnaSequences(s))
