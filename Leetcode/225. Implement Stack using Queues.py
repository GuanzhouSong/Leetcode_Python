class MyStack:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self._queue = list()

  def push(self, x):
    """
    Push element x onto stack.
    :type x: int
    :rtype: void
    """
    q = self._queue
    q = [x] + q

  def pop(self):
    """
    Removes the element on top of the stack and returns that element.
    :rtype: int
    """
    return self._queue.pop(-1)

  def top(self):
    """
    Get the top element.
    :rtype: int
    """
    return self._queue[-1]

  def empty(self):
    """
    Returns whether the stack is empty.
    :rtype: bool
    """
    return False if len(self._queue > 0) else True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
