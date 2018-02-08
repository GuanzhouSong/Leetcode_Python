# Definition for an interval.
class Interval:
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e


class Solution:
  def merge(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
      if out and i[0] <= out[-1][1]:
        out[-1][1] = max(out[-1][1], i[1])
      else:
        out.append(i)
    return out


s = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(s.merge(intervals))
