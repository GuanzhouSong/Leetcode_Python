class Solution:
  def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    start, end = 0, len(nums) - 1
    while start <= end:
      if nums[start] == val:
        nums[start], nums[end], end = nums[end], nums[start], end - 1
      else:
        start += 1
    return start


s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7]
print(s.removeElement(nums, 1))
