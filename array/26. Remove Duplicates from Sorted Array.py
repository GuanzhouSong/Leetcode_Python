class Solution:
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 1:
      return 0
    j = 0
    for i in range(len(nums)):
      if nums[i] != nums[j]:
        j += 1
        nums[j], nums[i] = nums[i], nums[j]
    return j + 1


s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7]
print(s.removeDuplicates(nums))
