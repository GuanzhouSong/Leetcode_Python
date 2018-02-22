class Solution:
  def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = ""
    while i >= 0 or j >= 0:
      sum = carry
      if i >= 0:
        sum += int(a[i])
        i -= 1
      if j >= 0:
        sum += int(b[j])
        j -= 1
      res = str(sum % 2) + res
      carry = sum // 2
    if carry != 0:
      res = str(carry) + res
    return res


s = Solution()
print(s.addBinary("100", "111"))
