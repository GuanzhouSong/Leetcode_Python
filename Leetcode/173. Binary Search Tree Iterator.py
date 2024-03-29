# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
  def __init__(self, root):
    """
    :type root: TreeNode
    """
    self.stack = list()
    self.pushall(root)

  def hasNext(self):
    """
    :rtype: bool
    """
    return self.stack

  def next(self):
    """
    :rtype: int
    """
    tempNode = self.stack.pop()
    self.pushall(tempNode)
    return tempNode.val()

  def pushall(self, node):
    while node is not None:
      self.stack.append(node)
      node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
