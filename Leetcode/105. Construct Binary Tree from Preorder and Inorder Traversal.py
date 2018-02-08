# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if inorder:
      index = inorder.index(preorder.pop(0))
      root = TreeNode(inorder[index])
      root.left = self.buildTree(preorder, inorder[0:index])
      root.right = self.buildTree(preorder, inorder[index + 1:])
      return root


s = Solution()
preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
print(s.buildTree(preorder, inorder).left.val)
