class Solution:
  def isInterleave(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    if len(s1) + len(s2) != len(s3):
      return False
    if len(s1) == 0 or len(s2) == 0:
      return True
    res = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    res[0][0] = True
    for i in range(1, len(res[0])):
      res[0][i] = (res[0][i - 1] and s1[i - 1] == s3[i - 1])
    for i in range(1, len(res)):
      res[i][0] = (res[i - 1][0] and s2[i - 1] == s3[i - 1])
    for i in range(1, len(res)):
      for j in range(1, len(res[0])):
        res[i][j] = (res[i - 1][j] and s2[i - 1] == s3[i + j - 1]) or (
            res[i][j - 1] and s1[j - 1] == s3[i + j - 1])
    return res[-1][-1]


s = Solution()
s1 = "aabccabc"
s2 = "dbbabc"
s3 = "aabdbbccababcc"
print(s.isInterleave(s1, s2, s3))
