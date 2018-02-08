class Solution:
  def subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]]
    nums.sort()
    for i in range(len(nums)):
      if i == 0 or nums[i] != nums[i - 1]:
        l = len(res)
      # 如果碰到重复的元素，则只对上一次循环新增的元素进行add
      for j in range(len(res) - l, len(res)):
        res.append(res[j] + [nums[i]])
    return res


s = Solution()
nums = [1, 2, 2]
print(s.subsetsWithDup(nums))
