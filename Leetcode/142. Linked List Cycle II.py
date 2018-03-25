# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
      return None
    slow, fast = head, head
    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        slow2 = head
        while slow != slow2:
          slow = slow.next
          slow2 = slow2.next
        return slow
    return None
