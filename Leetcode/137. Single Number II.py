class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    one, two = 0, 0
    for num in nums:
      one = (one ^ num) & ~two
      two = (two ^ num) & ~one
    return one


s = Solution()
nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
print(s.singleNumber(nums))
