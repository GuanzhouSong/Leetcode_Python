class Solution:
  def findUnsortedSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
      return 0
    sortednums = sorted(nums)
    s, e = 1, 0
    for i in range(len(nums)):
      if sortednums[i] != nums[i]:
        s = i
        break
    for i in range(len(nums) - 1, -1, -1):
      if sortednums[i] != nums[i]:
        e = i
        break
    return e - s + 1


s = Solution()
nums = [2, 1]
print(s.findUnsortedSubarray(nums))
