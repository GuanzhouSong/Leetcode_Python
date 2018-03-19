# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  res = 0

  def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
      return 0
    self.helper(root, 0)
    return self.res

  def helper(self, root, path):
    if root:
      self.helper(root.left, path * 10 + root.val)
      self.helper(root.right, path * 10 + root.val)
      if not root.left and not root.right:
        self.res += (path * 10 + root.val)

  def sumNumbersDFSStack(self, root):
    if not root:
      return 0
    stack = [(root, root.val)]
    res = 0
    while stack:
      node, value = stack.pop()
      if node:
        if not node.left and not node.right:
          res += value
        if node.right:
          stack.append((node.right, value * 10 + node.right.val))
        if node.left:
          stack.append((node.left, value * 10 + node.left.val))
    return res

  def sumNumbersBFSQueue(self, root):
    # the only difference with DFS is the left/right order
    if not root:
      return 0
    queue, res = [(root, root.val)], 0
    while queue:
      node, value = queue.pop(0)
      if node:
        if not node.left and not node.right:
          res += value
        if node.left:
          queue.append((node.left, value * 10 + node.left.val))
        if node.right:
          queue.append((node.right, value * 10 + node.right.val))
    return res


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.sumNumbersBFSQueue(root))
