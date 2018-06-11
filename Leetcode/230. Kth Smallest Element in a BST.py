# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    count = self.countNode(root)
    if k <= count:
      return self.kthSmallest(root.left, k)
    elif k > count + 1:
      return self.kthSmallest(root.right, k - 1 - count)

    return root.val

  def countNode(self, root):
    if root is None:
      return 0
    return self.countNode(root.left) + self.countNode(root.right)
