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

  def removeDuplicatesv3(self, nums):
    if len(nums) <= 2:
      return len(nums)
    count = 2
    for i in range(2, len(nums)):
      if nums[i] > nums[i - 2]:
        count += 1
    return count


s = Solution()
nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5]
nums2 = [1, 1, 1, 2]
print(s.removeDuplicatesv3(nums2))
