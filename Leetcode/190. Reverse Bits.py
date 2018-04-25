class Solution:
  # @param n, an integer
  # @return an integer
  def reverseBits(self, n):
    res = 0
    s = 1 << 31
    for i in range(32):
      if n << i & 1 != 0:
        res = res | s >> i
    return res
