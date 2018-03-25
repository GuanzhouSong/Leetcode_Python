class DLinkedList:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.pre = None
    self.post = None


class LRUCache:
  head, tail = DLinkedList(-1, -1), DLinkedList(-1, -1)
  dic = dict()
  count, capacity = 0, 0

  def addNode(self, node):
    node.pre = self.head
    node.post = self.head.post
    self.head.post.pre = node
    self.head.post = node

  def removeNode(self, node):
    preNode = node.pre
    postNode = node.post
    preNode.post = postNode
    postNode.pre = preNode

  def movetohead(self, node):
    self.removeNode(node)
    self.addNode(node)

  def poptail(self):
    res = self.tail.pre
    self.removeNode(res)
    return res

  def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.count = 0
    self.capacity = capacity
    self.head = DLinkedList
    self.head.pre = None
    self.tail = DLinkedList
    self.tail.post = None
    self.head.post = self.tail
    self.tail.pre = self.head

  def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    node = self.dic.get(key, None)
    if not node:
      return -1
    else:
      self.movetohead(node)
      return node.val

  def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: void
    """
    node = self.dic.get(key, None)
    if not node:
      node = DLinkedList(key, value)
      self.dic[key] = value
      self.addNode(node)
      self.count += 1
      if self.count > self.capacity:
        t = self.poptail()
        self.dic[t.key] = None
        self.count -= 1
    else:
      node.value = value
      self.movetohead(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
