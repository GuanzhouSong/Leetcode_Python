# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def invertTree1(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
      return None

    l, r = root.left.copy(), root.right.copy()
    root.left = self.invertTree(r)
    root.right = self.invertTree(l)

    return root

  def invertTree2(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
      return None

    s = list()
    s.append(root)

    while (len(s) > 0):
      node = s.pop()
      l, r = TreeNode(root.left.val), TreeNode(root.right.val)
      l.left, l.right = root.left.left, root.left.right
      r.left, r.right = root.right.left, root.right.right
      node.right = l
      node.left = node.right

      if node.left:
        s.append(node.left)

      if node.right:
        s.append(node.right)

    return root
