class Solution:
  def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    r = nums[0]
    imax = r
    imin = r
    for i in range(1, len(nums)):
      if nums[i] < 0:
        imin, imax = imax, imin
      imax = max(imax * nums[i], nums[i])
      imin = min(imin * nums[i], nums[i])
      r = max(r, imax)
    return r


s = Solution()
nums = [2, 3, -2, 4]
print(s.maxProduct(nums))
