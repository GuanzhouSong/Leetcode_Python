# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  import sys
  res = -1 * sys.maxsize

  def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.helper(root)
    return self.res

  def helper(self, root):
    if root is None:
      return 0
    l = max(0, self.helper(root.left))
    r = max(0, self.helper(root.right))
    self.res = max(self.res, l + r + root.val)
    return max(l, r) + root.val


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.maxPathSum(root))
