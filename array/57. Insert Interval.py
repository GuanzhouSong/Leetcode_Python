class Interval:
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e


class Solution:
  def insertByList(self, intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    intervals.append(newInterval)
    flag = 0
    pool = []
    stack = []
    res = []
    for i in intervals:
      pool.append([i[0], 0])
      pool.append([i[1], 1])
    pool.sort(key=lambda i: (i[0], i[1]))
    for i in pool:
      if i[1] == 0:
        flag += 1
        stack.append(i[0])
      if i[1] == 1:
        flag -= 1
        p = stack.pop()
      if flag is 0:
        res.append([p, i[0]])
    res.sort()
    return res

  def insert(self, intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    intervals.append(newInterval)
    flag = 0
    pool = []
    stack = []
    res = []
    for i in intervals:
      pool.append([i.start, 0])
      pool.append([i.end, 1])
    pool.sort(key=lambda i: i[0])
    for i in pool:
      if i[1] == 0:
        flag += 1
        stack.append(i[0])
      if i[1] == 1:
        flag -= 1
        p = stack.pop()
      if flag is 0:
        Interval(p, i[0])
        res.append()
    res.sort()
    return res


s = Solution()
intervals = [[1, 2], [3, 5], [8, 10], [12, 16]]
print(s.insertByList(intervals, [5, 7]))
