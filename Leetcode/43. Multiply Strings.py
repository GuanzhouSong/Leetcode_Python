class Solution:
  def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    m = len(num1)
    n = len(num2)
    pos = [0] * (m + n)
    for i in range(m - 1, -1, -1):
      for j in range(n - 1, -1, -1):
        v = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        p1, p2 = i + j, i + j + 1
        sum = v + pos[p2]
        pos[p1] += sum // 10
        pos[p2] = sum % 10
    res = ""
    for i in range(0, len(pos)):
      if len(res) != 0 or pos[i] != 0:
        res += str(pos[i])
    return res if len(res) > 0 else '0'


s = Solution()
print(s.multiply(num1="0", num2="0"))
