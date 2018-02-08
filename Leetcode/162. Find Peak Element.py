class Solution:
  def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(1, len(nums)):
      if nums[i - 1] > nums[i]:
        return nums[i - 1]
    return nums[-1]


s = Solution()
nums = [1, 2, 3, 4, 5, 8, 9]
print(s.findPeakElement(nums))
