class Solution:
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxnum = nums[0]
    current_sum = 0
    for num in nums:
      current_sum += num
      if current_sum > maxnum:
        maxnum = current_sum
      if current_sum < 0:
        current_sum = 0
    return maxnum


solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.maxSubArray(nums))
