# Definition for binary tree with next pointer.
class TreeLinkNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
    self.next = None


class Solution:
  # @param root, a tree link node
  # @return nothing
  def connect(self, root):
    if root is None:
      return
    else:
      level_start = root
      while level_start is not None:
        cur = level_start
        while cur is not None:
          if cur.left is not None:
            cur.left.next = cur.right
          if cur.right is not None and cur.next is not None:
            cur.right.next = cur.next.left
          cur = cur.next
        level_start = level_start.left
    return
