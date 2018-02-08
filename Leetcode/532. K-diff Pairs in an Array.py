class Solution:
  def findPairs(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if k == 0:
      s = set()
      l = [num for num in nums if num in s or s.add(num)]
      return len(set(l))
    elif k > 0:
      return len(set(nums) & set(n + k for n in nums))
    else:
      return 0


s = Solution()
nums = [1, 3, 1, 4, 6, 8, 1]
print(s.findPairs(nums, 0))
