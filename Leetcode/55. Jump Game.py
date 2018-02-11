class Solution:
  def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    reachable = 0
    n = len(nums)
    i = 0
    for i in range(n):
      if i > reachable:
        return False
      reachable = max(reachable, i + nums[i])
    return True


nums = [2, 0]
s = Solution()
print(s.canJump(nums))
