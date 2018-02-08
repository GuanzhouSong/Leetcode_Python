class Solution:
  def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
      return []
    num1, num2, count1, count2 = 0, 1, 0, 0
    for num in nums:
      if num1 == num:
        count1 += 1
      elif num2 == num:
        count2 += 1
      elif count1 == 0:
        num1, count1 = num, 1
      elif count2 == 0:
        num2, count2 = num, 1
      else:
        count1, count2 = count1 - 1, count2 - 1
    return [n for n in (num1, num2)
            if nums.count(n) > len(nums) // 3]


s = Solution()
print(s.majorityElement(nums=[1, 2]))
