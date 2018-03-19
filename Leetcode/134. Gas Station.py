class Solution(object):
  def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    sumCost, sumGas, start, tank = 0, 0, 0, 0
    for i in range(0, len(gas)):
      sumCost += cost[i]
      sumGas += gas[i]
      tank += gas[i] - cost[i]
      if tank < 0:
        tank = 0
        start = i + 1
    if sumGas < sumCost:
      return -1
    else:
      return start
