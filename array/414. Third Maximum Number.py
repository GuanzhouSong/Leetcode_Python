import sys


class Solution:
  def thirdMax(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max1, max2, max3 = -1 * sys.maxsize, -1 * sys.maxsize, -1 * sys.maxsize
    for num in nums:
      if num == max1 or num == max2 or num == max3:
        continue
      if num > max1:
        max3 = max2
        max2 = max1
        max1 = num
      elif num > max2:
        max3 = max2
        max2 = num
      elif num > max3:
        max3 = num

    return max3 if max3 != -sys.maxsize else max1


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(s.thirdMax(nums))
