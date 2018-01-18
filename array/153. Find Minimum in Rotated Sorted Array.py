class Solution:
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low = 0
    high = len(nums) - 1
    while low < high:
      mid = (low + high) // 2
      if nums[mid] > nums[high]:
        low = mid + 1
      else:
        high = mid
    return nums[low]

  def findMinv2(self, nums):
    import sys
    imin = sys.maxsize
    for num in nums:
      imin = min(imin, num)
    return imin


s = Solution()
nums = [3, 1, 2]
print(s.findMin(nums))
