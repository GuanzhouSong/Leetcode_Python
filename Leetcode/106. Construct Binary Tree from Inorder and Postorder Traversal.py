# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def buildTree(self, inorder, postorder):
    """
    :type postorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if inorder:
      index = inorder.index(postorder.pop(-1))
      root = TreeNode(inorder[index])
      root.right = self.buildTree(inorder[index + 1:], postorder)
      root.left = self.buildTree(inorder[0:index], postorder)
      return root


s = Solution()
postorder = [4, 5, 2, 6, 7, 3, 1]
inorder = [4, 2, 5, 1, 6, 3, 7]
print(s.buildTree(inorder, postorder).left.val)
