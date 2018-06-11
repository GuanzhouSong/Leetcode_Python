# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def countNodes(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
      return 0
    seen = set()

    def dfs(node):
      if node not in seen:
        seen.add(node)
      if node.left:
        dfs(node.left)
      if node.right:
        dfs(node.right)
      return

    dfs(root)
    return len(seen)

  def count(self, node):
    def getHeight(node):
      return -1 if node is None else getHeight(node.left) + 1

    h = getHeight(node)
    return 0 \
      if h < 0 \
      else \
      (1 << h) + self.count(node.right) \
        if getHeight(node.right) == h - 1 \
        else (1 << h - 1) + self.count(node.left)


"""
If yes, then the last node on the last tree row is in the right 
subtree and the left subtree is a full tree of height h-1. So we take 
the 2^h-1 nodes of the left subtree plus the 1 root node plus recursively
 the number of nodes in the right subtree.
If no, then the last node on the last tree row is in the left subtree and 
the right subtree is a full tree of height h-2. So we take the 2^(h-1)-1 nodes
 of the right subtree plus the 1 root node plus recursively the number of nodes in the left subtree.
"""

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(s.count(root))
