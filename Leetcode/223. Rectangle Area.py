class Solution:
  def computeArea(self, A, B, C, D, E, F, G, H):
    """
    :type A: int
    :type B: int
    :type C: int
    :type D: int
    :type E: int
    :type F: int
    :type G: int
    :type H: int
    :rtype: int
    """
    s1 = (C - A) * (D - B)
    s2 = (G - E) * (H - F)
    left = max(A, E)
    right = min(C, G)
    bottom = max(B, F)
    top = min(D, H)

    if right > left and top > bottom:
      overlap = (right - left) * (top - bottom)
    return s1 + s2 - overlap
