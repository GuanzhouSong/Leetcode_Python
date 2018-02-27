# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def generateTrees(self, n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    return self.helper(1, n)

  def helper(self, start, end):
    l = []
    if start > end:
      l.append(None)
      return l
    if start == end:
      l.append(TreeNode(start))
      return l
    for i in range(start, end + 1):
      leftl = self.helper(start, i - 1)
      rightl = self.helper(i + 1, end)
      for leftnode in leftl:
        for rightnode in rightl:
          root = TreeNode(i)
          root.left = leftnode
          root.right = rightnode
          l.append(root)
    return l


s = Solution()
l = s.generateTrees(3)
print(l)
