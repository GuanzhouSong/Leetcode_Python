class Solution:
  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    road=[[0 for i in range(n)] for i in range(m)]
    road[0][:]=[1 for i in range(n)]
    for i in range(m):
      road[i][0] = 1
    for i in range(1,m):
      for j in range(1,n):
        road[i][j] = road[i-1][j] + road[i][j-1]
    return road[m-1][n-1]

s=Solution()
print(s.uniquePaths(3,7))