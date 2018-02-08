class Solution:
  def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if len(grid) is 1 and len(grid[0]) is 1:
      return grid[0][0]
    m = len(grid)
    n = len(grid[0])
    # Initialization
    road = [[0 for i in range(n)] for i in range(m)]
    # 处理边界问题
    road[0][0] = grid[0][0]
    for i in range(1, n):
      road[0][i] = road[0][i - 1] + grid[0][i]
    for i in range(1, m):
      road[i][0] = road[i - 1][0] + grid[i][0]
    # DP
    for i in range(1, m):
      for j in range(1, n):
        road[i][j] = min(road[i - 1][j], road[i][j - 1]) + grid[i][j]
    return road[m - 1][n - 1]


s = Solution()
feedin = [[1, 3, 1],
          [1, 5, 1],
          [4, 2, 1]]
print(s.minPathSum(feedin))
