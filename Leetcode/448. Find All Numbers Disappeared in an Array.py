class Solution:
  def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for i in range(0, len(nums)):
      idx = abs(nums[i]) - 1
      if nums[idx] > 0:
        nums[idx] = -nums[idx]
    for i in range(0, len(nums)):
      if nums[i] > 0:
        res.append(i + 1)
    return res

  def findDisappearedNumbers2(self, nums):
    return list(set(list(range(1, len(nums) + 1))) - set(nums))


s = Solution()
nums = [1, 2, 2, 3, 4, 7, 8, 8]
print(s.findDisappearedNumbers2(nums))
