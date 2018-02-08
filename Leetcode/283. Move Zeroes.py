class Solution:
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0
    for i in range(0, len(nums)):
      if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1

  def moveZeroes2(self, nums):
    i = 0
    for num in nums:
      if num != 0:
        nums[i] = num
        i += 1
    for j in range(i, len(nums)):
      nums[j] = 0


s = Solution()
nums = [0, 1, 0, 3, 12]
nums2 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
s.moveZeroes2(nums2)
print(nums2)
