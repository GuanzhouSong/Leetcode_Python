# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    res = ListNode(0)
    p = res
    while l1 and l2:
      if l1.val < l2.val:
        p.next = ListNode(l1.val)
        p = p.next
        l1 = l1.next
      else:
        p.next = ListNode(l2.val)
        p = p.next
        l2 = l2.next
    if l1:
      p.next = l1
    if l2:
      p.next = l2
    return res.next
