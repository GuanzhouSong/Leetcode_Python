# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if len(nums) < 1:
      return None
    return self.helper(nums, 0, len(nums) - 1)

  def helper(self, num, low, high):
    if low > high:
      return None
    mid = low + (high - low) // 2
    root = TreeNode(num[mid])
    root.left = self.helper(num, low, mid - 1)
    root.right = self.helper(num, mid + 1, high)
    return root
