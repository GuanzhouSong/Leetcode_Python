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
    point = head
    while point.next:
      if point.val == point.next.val:
        point.next = point.next.next
      else:
        point = point.next
    return head


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
s = Solution()
print(s.deleteDuplicates(head).next.val)
