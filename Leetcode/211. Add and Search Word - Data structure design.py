from collections import defaultdict


class Node:
  def __init__(self):
    self.children = defaultdict(Node)
    self.isEndwith = False


class WordDictionary:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = Node()

  def addWord(self, word):
    """
    Adds a word into the data structure.
    :type word: str
    :rtype: void
    """
    cur = self.root
    for c in word:
      cur = cur.children[c]
    cur.isEndwith = True

  def search(self, word):
    """
    Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
    :type word: str
    :rtype: bool
    """
    cur = self.root
    for i, l in enumerate(word):
      if l == '.':
        for k in cur.children:
          chdTrie = WordDictionary()
          chdTrie.root = cur.children[k]
          if chdTrie.search(word[i + 1:]):
            return True
        return False
      elif l not in cur.children:
        return False
      cur = cur.children[l]
    return cur.isEndwith

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
