# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def insertionSortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
      return head
    else:
      dummy = ListNode(0)
      cur = head
      pre = dummy
      next = None
      while cur:
        next = cur.next
        while pre.next and pre.next.val < cur.val:
          pre = pre.next
        cur.next = pre.next
        pre.next = cur
        cur = next
    return dummy.next
