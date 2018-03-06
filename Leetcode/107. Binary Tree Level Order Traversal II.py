# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    queue, res = [], []
    if root is None:
      return res
    queue.append(root)
    while len(queue) > 0:
      length = len(queue)
      temp = []
      for _ in range(length):
        cur = queue.pop(0)
        if cur.left is not None:
          queue.append(cur.left)
        if cur.right is not None:
          queue.append(cur.right)
        temp += [cur.val]
      res.append(temp)
    res.reverse()
    return res
