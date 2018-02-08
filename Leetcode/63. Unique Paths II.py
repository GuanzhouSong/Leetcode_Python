class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if len(obstacleGrid) is 1 and len(obstacleGrid[0]) is 1:
      if obstacleGrid[0][0] == 1:
        return 0
      else:
        return 1
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    road = [[0 for i in range(n)] for i in range(m)]
    # 处理边界问题
    for i in range(n):
      if obstacleGrid[0][i] is not 1:
        road[0][i] = 1
      else:
        break
    for i in range(m):
      if obstacleGrid[i][0] is not 1:
        road[i][0] = 1
      else:
        break
    # DP
    for i in range(1, m):
      for j in range(1, n):
        if obstacleGrid[i][j] is not 1:
          road[i][j] = road[i - 1][j] + road[i][j - 1]
        else:
          road[i][j] = 0
    return road[m - 1][n - 1]


s = Solution()
obstacle = [[1, 0]
            ]
print(s.uniquePathsWithObstacles(obstacle))
