class Solution:
  def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:
      return [-1, -1]

    def search(left, right):
      if nums[left] == target == nums[right]:
        return [left, right]
      if nums[left] <= target <= nums[right]:
        mid = (left + right) // 2
        l, r = search(left, mid), search(mid + 1, right)
        return max(l, r) if -1 in l + r else [l[0], r[1]]
      return [-1, -1]

    return search(0, len(nums) - 1)


s = Solution()
nums = []
print(s.searchRange(nums, 0))
