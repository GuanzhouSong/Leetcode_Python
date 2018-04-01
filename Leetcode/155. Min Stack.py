class element:
  def __init__(self, value, minValue):
    self.value = value
    self.minValue = minValue


class MinStack:
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.s = []

  def push(self, x):
    """
    :type x: int
    :rtype: void
    """
    minValue = min(self.s[-1].minValue, x) if len(self.s) > 0 else x
    self.s.append(element(x, minValue))

  def pop(self):
    """
    :rtype: void
    """
    self.s.pop()

  def top(self):
    """
    :rtype: int
    """
    return self.s[-1].value

  def getMin(self):
    """
    :rtype: int
    """
    return self.s[-1].minValue


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
