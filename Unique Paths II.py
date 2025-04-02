class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        memo = {}
        def dp(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1 or obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1  
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = dp(i,j+1) + dp(i+1,j)
            return memo[(i,j)]
        
        return dp(0,0)