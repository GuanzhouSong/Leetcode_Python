# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
      return True
    stack = []
    pre = None
    while root != None or len(stack) == 0:
      while root != None:
        stack.append(root)
        root = root.left
      root = stack.pop()
      if pre != None and root.val <= pre.val:
        return False
      pre = root
      root = root.right
    return True
