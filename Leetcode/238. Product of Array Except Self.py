class Solution:
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
      return []
    res = [1]
    for i in range(1, len(nums)):
      temp = res[i - 1] * nums[i - 1]
      res.append(temp)
    right = 1
    for i in range(len(nums) - 1, -1, -1):
      res[i] *= right
      right *= nums[i]
    return res


s = Solution()
print(s.productExceptSelf(nums=[1, 2, 3, 4, 5]))
