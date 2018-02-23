# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
      return head
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = head
    while fast:
      while fast.next and fast.val == fast.next.val:
        fast = fast.next
      if slow.next == fast:
        slow = slow.next
      else:
        slow.next = fast.next
      fast = fast.next
    return dummy.next


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
s = Solution()
print(s.deleteDuplicates(head).val)
