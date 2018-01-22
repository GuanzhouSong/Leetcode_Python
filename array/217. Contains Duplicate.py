class Solution:
  def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 0:
      return False
    m = dict()
    for num in nums:
      temp = m.get(num, 0)
      if temp != 0:
        return True
      m[num] = 1
    return False

  def containsDuplicatev2(self, nums):
    s = set(nums)
    return len(s) != len(nums)


s = Solution()
nums = [1, 1, 2, 3, 4, 5, 6]
print(s.containsDuplicatev2(nums))
