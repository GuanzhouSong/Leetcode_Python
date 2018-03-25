# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack = [], []
    if not root:
      return res
    stack.append(root)
    while stack:
      curr = stack.pop()
      res = [curr.val] + res
      if curr.left:
        stack.append(curr.left)
      if curr.right:
        stack.append(curr.right)
    return res

  def recursivehelper(self, root, res):
    if not root:
      return
    self.recursivehelper(root.left, res)
    self.recursivehelper(root.right, res)
    res.append(root.val)

  def recursive(self, root):
    res = []
    self.recursivehelper(root, res)
    return res


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.right = node1
node1.left = node2
s = Solution()
print(s.postorderTraversal(root))
