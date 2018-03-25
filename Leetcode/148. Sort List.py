# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
      return head
    # cut in half
    slow, fast = head, head
    while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next
    prev.next = None
    # sort each half
    l1 = self.sortList(head)
    l2 = self.sortList(slow)
    # merge
    return self.merge(l1, l2)

  def merge(self, l1, l2):
    dummy = ListNode(0)
    p = dummy
    while l1 and l2:
      if l1.val < l2.val:
        p.next = l1
        l1 = l1.next
      else:
        p.next = l2
        l2 = l2.next
      p = p.next
    if l1:
      p.next = l1
    if l2:
      p.next = l2
    return dummy.next
