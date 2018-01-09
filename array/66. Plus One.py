class Solution:
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num = 0
    while len(digits) > 0:
      num = num * 10 + digits.pop(0)
    num += 1
    res = []
    while num >= 10:
      res.append(num % 10)
      num = num // 10
    res.append(num % 10)
    res.reverse()
    return res

  def plusOnev2(self, digits):
    digits[-1] += 1
    for i in range(len(digits) - 1, 0, -1):
      if digits[i] == 10:
        digits[i - 1] += 1
        digits[i] = 0
    if digits[0] == 10:
      digits = [1, 0] + digits[1:]
    return digits


s = Solution()
print(s.plusOnev2([9, 9, 9, 9]))
