# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def reverseListit(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head:
      curr = head
      head = head.next
      curr.next = prev
      prev = curr
    return prev

  def reverseList(self, head):
    return self._recursive(head)

  def _recursive(self, node, prev=None):
    if not node:
      return prev
    n = node.next
    node.next = prev
    self._recursive(n, node)


s = Solution()
n = ListNode(0)
print(s.reverseList(n))
