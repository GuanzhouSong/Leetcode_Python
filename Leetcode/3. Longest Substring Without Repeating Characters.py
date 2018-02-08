class Solution:
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    j = 0
    res = 0
    dic = dict()
    l = list(s)
    for i in range(len(l)):
      if l[i] in dic:
        j = max(j, dic.get(l[i]) + 1)
      dic[l[i]] = i
      res = max(res, i - j + 1)
    return res


s = Solution()
nums = "abcadfa"
print(s.lengthOfLongestSubstring(nums))
