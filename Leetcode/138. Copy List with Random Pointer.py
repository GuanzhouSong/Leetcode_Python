# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
  def __init__(self, x):
    self.label = x
    self.next = None
    self.random = None


class Solution(object):
  def copyRandomList(self, head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """

    node = head
    while node:
      copy = RandomListNode(node.label)
      copy.next = node.next
      node.next = copy
      node = copy.next
    node = head
    while node:
      node.next.random = node.random and node.random.next
      node = node.next.next
    iter = head
    dummy = RandomListNode(0)
    copyiter = dummy
    while iter:
      copyiter.next = iter.next
      copyiter = copyiter.next
      iter.next = iter.next.next
      iter = iter.next
    return dummy.next
