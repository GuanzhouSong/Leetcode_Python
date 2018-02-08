class Solution:
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    res = [""]
    dic = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}
    l = len(digits)
    if l < 1:
      return []
    res = self.helper(dic, digits, 0, res)
    return res

  def helper(self, dic, digits, i, res):
    if i >= len(digits):
      return res
    l = dic[digits[i]]
    temp = []
    for c in l:
      temp += [x + c for x in res]
    res = temp.copy()
    return self.helper(dic, digits, i + 1, res)


s = Solution()
print(s.letterCombinations("23"))
