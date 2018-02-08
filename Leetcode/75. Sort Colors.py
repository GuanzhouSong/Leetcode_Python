class Solution:
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    zeropos = 0
    secondpos = n - 1
    for i in range(n):
      while nums[i] == 2 and i < secondpos:
        nums[i], nums[secondpos] = nums[secondpos], nums[i]
        secondpos -= 1
      while nums[i] == 0 and i > zeropos:
        nums[i], nums[zeropos] = nums[zeropos], nums[i]
        zeropos += 1


s = Solution()
nums = [0, 0]
s.sortColors(nums)
print(nums)
