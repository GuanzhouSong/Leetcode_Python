class Node(object):
  def __init__(self, val=None):
    self.val = val
    self.children = {}
    self.isEndWith = False


class Trie:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = Node()

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    if not word:
      return
    root = self.root
    for c in word:
      if c not in root.children:
        root.children[c] = Node(c)
      root = root.children[c]
    root.isEndWith = True
    return

  def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    if not word:
      return False
    root = self.root
    for c in word:
      if c not in root.children:
        return False
      root = root.children[c]
    return root.isEndWith == True

  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    if not prefix:
      return False

    root = self.root
    for char in prefix:
      if char not in root.children:
        return False
      root = root.children[char]
    return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
