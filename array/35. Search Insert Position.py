class Solution:
  def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    min = 0
    max = len(nums) - 1;
    while min <= max:
      pos = (min + max) // 2
      if nums[pos] == target:
        return pos
      elif nums[pos] < target:
        min = pos + 1
      else:
        max = pos - 1
    return min

  def searchInsert2(self, nums, target):
    return len([x for x in nums if x < target])

  nums = [1, 2, 5, 6]
  target = 7
  print(searchInsert(0, nums, target))
  print(searchInsert2(0, nums, target))
