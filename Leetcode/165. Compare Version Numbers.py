class Solution:
  def compareVersion(self, version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    num1, num2 = version1.split('.'), version2.split('.')
    length = max(len(num1), len(num2))
    for i in range(0, length):
      n1 = int(num1[i]) if i < len(num1) else 0
      n2 = int(num2[i]) if i < len(num2) else 0
      if n1 > n2:
        return 1
      elif n1 < n2:
        return -1
    return 0


s = Solution()
print(s.compareVersion("1", "01"))
