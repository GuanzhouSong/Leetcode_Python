# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution(object):
  def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack = [], []
    while root:
      res.append(root.val)
      if root.right is not None:
        stack.append(root.right)
      root = root.left
      if root is None and len(stack) > 0:
        root = stack.pop()
    return res


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.right = node1
node1.left = node2
s = Solution()
print(s.preorderTraversal(root))
"""
There is an universal idea for preorder traversal inorder traversal and 
postorder traversal. For each node N, we process it as follows:-------
push N in stack -> push left tree of N in stack -> pop left tree of N -> 
push right tree of N in stack -> pop right tree of N -> pop N---------
For preorder traversal, we visit a node when pushing it in stack. For inorder 
traversal, we visit a node when pushing its right child in stack. 
for postorder traversal, we visit a node when popping it. last_pop represents 
the node which is popped the last time. For the top node in stack, it has three choices, 
pushing its left child in stack, or pushing its right child in stack, or being popped. 
If last_pop != top->left, meaning that its left tree has not been pushed in stack, 
then we push its left child. If last_pop == top->left, we push its right child. 
Otherwise, we pop the top node.
"""
