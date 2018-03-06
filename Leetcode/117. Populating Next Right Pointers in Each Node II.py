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
    head, prev = None, None
    cur = root
    while cur is not None:
      while cur is not None:
        if cur.left is not None:
          if prev is not None:
            prev.next = cur.left
          else:
            head = cur.left
          prev = cur.left
        if cur.right is not None:
          if prev is not None:
            prev.next = cur.right
          else:
            head = cur.right
          prev = cur.right
        cur = cur.next

      cur = head
      head, prev = None, None
