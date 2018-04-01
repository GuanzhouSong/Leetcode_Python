# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):
  def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    p1, p2 = headA, headB
    count1, count2 = 0, 0
    while p1:
      count1 += 1
      p1 = p1.next
    while p2:
      count2 += 1
      p2 = p2.next
    p1, p2 = headA, headB
    while count1 > count2:
      p1 = p1.next
      count1 -= 1
    while count1 < count2:
      p2 = p2.next
      count2 -= 1
    while p1 != p2:
      p1, p2 = p1.next, p2.next
    return p1
