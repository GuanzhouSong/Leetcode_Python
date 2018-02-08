class Solution:
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(numbers) - 1
    res = []
    if len(numbers) < 2 or numbers == None:
      return res
    while left < right:
      t = numbers[left] + numbers[right]
      if t == target:
        res.append(left + 1)
        res.append(right + 1)
        break
      if t > target:
        right -= 1
      else:
        left += 1
    return res

  def twoSumv2(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = dict()
    res = []
    if len(numbers) < 2 or numbers == None:
      return res
    for i in range(len(numbers)):
      t = target - numbers[i]
      if t in dic:
        res.append(dic.get(t) + 1)
        res.append(i + 1)
      dic[numbers[i]] = i
    return res


s = Solution()
nums = [2, 3, 4]
print(s.twoSumv2(nums, 6))
