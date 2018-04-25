class Solution(object):
  def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    yes, no = [0 for _ in range(len(nums) + 1)], [0 for _ in
                                                  range(len(nums) + 1)]
    yes[0], no[0] = 0, 0
    for i in range(1, len(nums) + 1):
      no[i] = max(yes[i - 1], no[i - 1])
      yes[i] = nums[i - 1] + no[i - 1]
    return max(no[-1], yes[-1])
