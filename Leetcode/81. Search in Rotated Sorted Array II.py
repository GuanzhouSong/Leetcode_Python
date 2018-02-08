class Solution:
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    start = 0
    end = len(nums) - 1
    mid = -1
    while start <= end:
      mid = (start + end) // 2
      if nums[mid] == target:
        return True
      if nums[mid] < nums[end] or nums[mid] < nums[start]:
        if nums[mid] < target <= nums[end]:
          start = mid + 1
        else:
          end = mid - 1
      elif nums[mid] > nums[start] or nums[mid] > nums[end]:
        if nums[mid] > target >= nums[start]:
          end = mid - 1
        else:
          start = mid + 1
      else:
        end -= 1
    return False


s = Solution()
nums = [7, 8, 9, 0, 1, 2, 2, 3, 4, 4, 5, 6, 7]
print(s.search(nums, 7))
