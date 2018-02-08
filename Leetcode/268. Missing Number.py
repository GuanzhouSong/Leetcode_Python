class Solution:
  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    return (n + 1) * n // 2 - sum(nums)


s = Solution()
print(s.missingNumber(nums=[0, 1, 2, 4, 5, 6, 7, 8]))
