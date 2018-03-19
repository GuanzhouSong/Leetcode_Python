class Solution(object):
  def candy(self, ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    size = len(ratings)
    if size < 2:
      return size
    res = [1 for _ in range(size)]
    for i in range(1, size):
      if ratings[i - 1] < ratings[i]:
        res[i] = res[i - 1] + 1
    for i in range(size - 1, 0, -1):
      if ratings[i - 1] > ratings[i]:
        res[i - 1] = max(res[i] + 1, res[i - 1])
    return sum(res)
