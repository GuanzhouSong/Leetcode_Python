import sys


class Solution:
  def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    res = sys.maxsize
    nums.sort()
    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      l, r = i + 1, len(nums) - 1
      while l < r:
        s = nums[l] + nums[i] + nums[r]
        if s < target:
          l += 1
          res = s if abs(s - target) < abs(res - target) else res
        elif s > target:
          r -= 1
          res = s if abs(s - target) < abs(res - target) else res
        else:
          return target
    return res


s = Solution()
nums = [-1, 2, 1, -4]
print(s.threeSumClosest(nums, 1))
