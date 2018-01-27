class Solution:
  def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    res = 0
    for i in range(0, len(nums), 2):
      res += nums[i]
    return res


s = Solution()
nums = [1, 4, 3, 2]
print(s.arrayPairSum(nums))
