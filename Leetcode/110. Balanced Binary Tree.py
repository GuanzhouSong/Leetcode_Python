# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
      return True
    l, r = 0, 0
    if root.left is not None:
      l = self.helper(root.left) + 1
    if root.right is not None:
      r = self.helper(root.right) + 1
    return abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(
      root.right)

  def helper(self, root):
    if root is None:
      return True
    l, r = 0, 0
    if root.left is not None:
      l = self.helper(root.left) + 1
    if root.right is not None:
      r = self.helper(root.right) + 1
    return max(l, r)
