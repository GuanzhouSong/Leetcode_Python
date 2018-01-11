class Solution:
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = dict()
    n = []
    for i in nums:
      if int(dic.get(i, 0)) < 2:
        dic[i] = dic.get(i, 0) + 1
        n.append(i)
    return n

  def removeDuplicatesv2(self, nums):
    i = 2
    for n in nums:
      if n > nums[i - 2]:
        nums[i] = n
        i += 1
    return i


s = Solution()
nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5]
print(s.removeDuplicatesv2(nums))
