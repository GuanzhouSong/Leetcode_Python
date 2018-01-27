class Solution:
  def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    dic = {0: 1}
    total, res = 0, 0
    for i in range(len(nums)):
      total += nums[i]
      res += dic.get(total - k, 0)
      dic[total] = dic.get(total, 0) + 1
    return res


s = Solution()
nums = [1, 1, 1]
print(s.subarraySum(nums, 2))
