# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return root is None or self.helper(root.left, root.right)

  def helper(self, left, right):
    if left is None or right is None:
      return left == right
    if left.val != right.val:
      return False
    return (self.helper(left.left, right.right) and self.helper(left.rught,
                                                                right.left))
