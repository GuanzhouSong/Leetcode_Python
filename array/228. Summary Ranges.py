class Solution:
  def summaryRanges(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if len(nums) < 1:
      return []
    l = []
    res = []
    i = 0
    while i < len(nums):
      if len(l) == 0 or nums[i] == l[-1] + 1:
        l.append(nums[i])
        i += 1
      else:
        if len(l) > 1:
          s = str(l[0]) + "->" + str(l[-1])
        else:
          s = str(l[0])
        res.append(s)
        l.clear()
    if len(l) > 1:
      s = str(l[0]) + "->" + str(l[-1])
    else:
      s = str(l[0])
    res.append(s)
    return res


s = Solution()
nums = [0, 1, 2, 3, 5, 6, 7, 9, 11]
print(s.summaryRanges(nums))
