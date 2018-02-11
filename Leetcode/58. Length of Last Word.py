class Solution:
  def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 1:
      return 0
    else:
      count = 0
      end = len(s) - 1
      while s[end] == " " and end > 0:
        end -= 1
      for i in range(end, -1, -1):
        if s[i] != " ":
          count += 1
        else:
          return count
      return count


s = Solution()
print(s.lengthOfLastWord(" "))
