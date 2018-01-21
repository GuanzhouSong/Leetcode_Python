class Solution:
  def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
      return None
    dic = dict()
    n = len(nums)
    for num in nums:
      count = dic.get(num, 0)
      count += 1
      dic[num] = count
      if count > n / 2:
        return num
    return None

  def majorityElementv2(self, nums):
    for i in nums:
      if (nums.count(i)) > len(nums) // 2: return i


s = Solution()
nums = [1, 2, 1, 1, 1, 4, 5, 1, 7]
print(s.majorityElementv2(nums))
