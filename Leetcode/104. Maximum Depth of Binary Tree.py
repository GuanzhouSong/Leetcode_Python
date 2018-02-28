# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    queue = []
    res = 0
    if root is None:
      return res
    queue.append(root)
    sign = 0
    while len(queue) > 0:
      length = len(queue)
      temp = []
      for _ in range(length):
        cur = queue.pop(0)
        if cur.left is not None:
          queue.append(cur.left)
        if cur.right is not None:
          queue.append(cur.right)
      res += 1
    return res
