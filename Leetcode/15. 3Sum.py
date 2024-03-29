"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
      l, r = i + 1, len(nums) - 1
      while l < r:
        s = nums[l] + nums[i] + nums[r]
        if s < 0:
          l += 1
        elif s > 0:
          r -= 1
        else:
          res.append([nums[i], nums[l], nums[r]])
          while l < r and nums[l] == nums[l + 1]:
            l += 1
          while l < r and nums[r] == nums[r - 1]:
            r -= 1
          l += 1
          r -= 1
    return res


s = Solution()
nums = [0, 0, 0]
print(s.threeSum(nums))
