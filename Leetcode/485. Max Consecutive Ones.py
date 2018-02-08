class Solution:
  def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    imax = 0
    res = 0
    for i in range(0, len(nums)):
      if nums[i] == 0:
        imax = max(imax, res)
        res = 0
      else:
        res += 1

    return imax


s = Solution()
nums = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
print(s.findMaxConsecutiveOnes(nums))
