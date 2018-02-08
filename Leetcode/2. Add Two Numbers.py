# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    res = n = ListNode(0)
    while l1 or l2 or carry:
      val1 = val2 = 0
      if l1:
        val1 = l1.val
        l1 = l1.next
      if l2:
        val2 = l2.val
        l2 = l2.next
      val = (val1 + val2 + carry) % 10
      carry = (val1 + val2 + carry) // 10
      n.next = ListNode(val)
      n = n.next

    return res.next


s = Solution()
l1 = ListNode(5)
l2 = ListNode(5)
print(s.addTwoNumbers(l1, l2).next.val)
