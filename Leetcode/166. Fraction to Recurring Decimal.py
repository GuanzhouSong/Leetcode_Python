class Solution:
  def fractionToDecimal(self, numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    if numerator == 0:
      return "0"
    res = []
    if numerator / denominator < 0:
      res.append("-")
    num, den = abs(numerator), abs(denominator)
    res.append(str(num // den))
    num %= den
    if num == 0:
      return "".join(res)

    res.append(".")
    dic = dict()
    dic[num] = len(res)
    while num != 0:
      num *= 10
      res.append(str(num // den))
      num %= den
      if num in dic:
        index = dic.get(num)
        res.insert(index, "(")
        res.append(")")
        break
      else:
        dic[num] = len(res)
    return "".join(res)


s = Solution()
print(s.fractionToDecimal(6, 4))
