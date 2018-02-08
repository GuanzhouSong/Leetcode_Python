class Solution:
  def arrayNesting(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i in range(len(nums)):
      k = i
      size = 0
      while nums[k] >= 0:
        size += 1
        index = nums[k]
        nums[k] = -1
        k = index
      res = max(res, size)
    return res


s = Solution()
nums = [0, 1, 2]
print(s.arrayNesting(nums))
