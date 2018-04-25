class Solution:
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:k], nums[k:] = nums[n - k:], nums[:n - k]


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(nums, 3)
print(nums)
