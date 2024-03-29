class Solution:
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    dic = dict()
    for num in nums:
      if dic.get(num, 0):
        continue
      # 不可能存在n-1为边界的连续序列包含n的情况因为这里已经确定num没有访问过n
      left = dic.get(num - 1, 0)
      right = dic.get(num + 1, 0)
      sum = left + right + 1
      dic[num] = sum

      res = max(sum, res)

      dic[num - left] = sum
      dic[num + right] = sum
    return res


s = Solution()
nums = [100, 1, 200, 2, 4, 3, 34, 342, 23, 65, 5, 35]
print(s.longestConsecutive(nums))
