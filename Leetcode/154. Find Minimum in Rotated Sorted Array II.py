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
      elif nums[mid] < nums[high]:
        high = mid
      else:
        high -= 1
    return nums[low]


s = Solution()
nums = [3, 1, 2, 2, 2, 3]
print(s.findMin(nums))
