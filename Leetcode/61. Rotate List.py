# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
      return None
    if not head.next:
      return head
    pointer = head
    length = 1
    while pointer.next:
      length += 1
    rotatetimes = k % length
    if rotatetimes == 0:
      return head
    fast = head
    slow = head
    for _ in range(rotatetimes):
      fast = fast.next
    while fast.next:
      fast = fast.next
      slow = slow.next
    temp = slow.next
    slow.next = None
    fast.next = head
    head = temp
    return head
