class Solution:
  def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if len(nums) == 0:
      return False
    m = dict()
    for i in range(len(nums)):
      temp = m.get(nums[i], -1)
      if temp != -1 and abs(i - temp) <= k:
        return True
      m[nums[i]] = i
    return False


s = Solution()
print(s.containsNearbyDuplicate(nums=[-1, -1], k=1))
