# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    res, path = [], []
    self.helper(root, sum, path, res)
    return res

  def helper(self, root, sum, path, res):
    if root is None:
      return
    path.append(root.val)
    if root.left is None and root.right is None and root.val - sum == 0:
      res.append(path)
      path.pop()
      return
    else:
      self.helper(root.left, sum - root.val, path, res)
      self.helper(root.right, sum - root.val, path, res)
    path.pop()
    return
