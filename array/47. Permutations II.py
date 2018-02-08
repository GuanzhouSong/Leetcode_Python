class Solution:
  def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    res = []
    rec = [False] * len(nums)
    self.helper(nums, rec, [], res)
    return res

  def helper(self, nums, rec, temp, res):
    if len(temp) == len(nums):
      res.append(temp.copy())
    else:
      for i in range(len(nums)):
        if rec[i]:
          continue
        if i > 0 and nums[i] == nums[i - 1] and rec[i - 1] is True:
          continue
        rec[i] = True
        temp.append(nums[i])
        self.helper(nums, rec, temp, res)
        rec[i] = False
        temp.pop()


s = Solution()
nums = [1, 1]
print(s.permuteUnique(nums))
