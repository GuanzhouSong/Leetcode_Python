class Solution:
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    self.helper(nums, [], res)
    return res

  def helper(self, nums, temp, res):
    if len(temp) == len(nums):
      res.append(temp.copy())
    else:
      for i in range(len(nums)):
        if nums[i] in temp:
          continue
        temp.append(nums[i])
        self.helper(nums, temp, res)
        temp.pop()


s = Solution()
nums = [1, 2, 3]
print(s.permute(nums))
