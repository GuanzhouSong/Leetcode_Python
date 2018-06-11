class Solution:
  def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
      return sum(nums)
    return max(self.helper(nums[1:]), self.helper(nums[:-1]))

  def helper(self, nums):
    cur, last = 0, 0
    for i in nums:
      temp = cur
      cur = max(cur, last + i)
      last = temp
    return cur


s = Solution()
nums = [1, 2, 3, 1]
print(s.rob(nums))
