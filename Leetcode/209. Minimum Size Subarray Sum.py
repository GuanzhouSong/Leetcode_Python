class Solution:
  def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    import sys
    n = len(nums)
    left = 0
    total = 0
    res = sys.maxsize
    for i in range(0, n):
      total += nums[i]
      while total >= s:
        res = min(res, i + 1 - left)
        total -= nums[left]
        left += 1

    return res if res != sys.maxsize else 0


s = Solution()
nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
print(s.minSubArrayLen(213, nums))
