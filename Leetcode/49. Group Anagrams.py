class Solution:
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = dict()
    for s in strs:
      c = sorted(list(s))
      val = dic.get(tuple(c), [])
      val += [s]
      dic[tuple(c)] = val
    return list(dic.values())


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))
