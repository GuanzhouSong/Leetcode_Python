# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def partition(self, head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    dummyless, dummymore = ListNode(0), ListNode(0)
    pless, pmore = dummyless, dummymore
    while head:
      if head.val < x:
        pless.next = head
        pless = pless.next
      else:
        pmore.next = head
        pmore = pmore.next
      head = head.next
    pmore.next = None
    pless.next = dummymore.next
    return dummyless.next
