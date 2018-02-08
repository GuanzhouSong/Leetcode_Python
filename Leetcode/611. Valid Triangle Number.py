class Solution:
  def triangleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    nums.sort()
    count = 0
    for i in range(len(nums)):
      l, r = 0, i - 1
      while l < r:
        if nums[l] + nums[r] > nums[i]:
          count += r - l
          r -= 1
        else:
          l += 1
    return count


s = Solution()
nums = [2, 2, 3, 4]
print(s.triangleNumber(nums))
