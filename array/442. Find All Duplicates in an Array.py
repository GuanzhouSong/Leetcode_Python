class Solution:
  def findDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for i in range(0, len(nums)):
      idx = abs(nums[i]) - 1
      if nums[idx] > 0:
        nums[idx] = -nums[idx]
      else:
        res.append(idx + 1)
    return res

  def findDuplicates2(self, nums):
    s = set()
    return [
      num for num in nums if num in s or s.add(num)
    ]
  # 第一次遇见不返回，但是加入set，第二次遇见才会被添加进res


s = Solution()
nums = [1, 2, 2, 3, 4, 5, 6, 7, 7]
print(s.findDuplicates(nums))

