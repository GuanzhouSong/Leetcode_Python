class Solution:
  def combinationSum3(self, k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []
    temp = []
    self.helper(res, temp, nums, n, k, 0)
    return res

  def helper(self, res, temp, nums, n, k, start):
    if k == 0 and n == 0:
      res.append(temp.copy())
    else:
      for i in range(start, 9):
        if k <= 0 or n <= 0:
          break
        temp.append(nums[i])
        self.helper(res, temp, nums, n - nums[i], k - 1, i + 1)
        temp.pop(-1)


s = Solution()
print(s.combinationSum3(3, 9))
