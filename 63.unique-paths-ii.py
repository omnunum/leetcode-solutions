#
# @lc app=leetcode id=63 lang='python3'
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    from functools import cache
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        
        # @cache
        # def travel(y: int, x: int) -> int:
        #     bottom_edge, right_edge = y == m - 1, x == n - 1
        #     if bottom_edge and right_edge:
        #         return 1
        #     right_solutions = down_solutions = 0
        #     if not right_edge and obstacleGrid[y][x+1] == 0:
        #         right_solutions = travel(y, x+1)
        #     if not bottom_edge and obstacleGrid[y+1][x] == 0:
        #         down_solutions = travel(y+1, x)
        #     return down_solutions + right_solutions
        # return travel(0,0)
        
        # Bottom-Up 
        dp = [[0] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                up, left = max(0, y-1), max(0, x-1)
                if obstacleGrid[y][x] == 1:
                    continue
                elif (y,x) == (0,0):
                    dp[y][x] = 1
                else:
                    dp[y][x] = dp[y][left] + dp[up][x]
        return dp[m-1][n-1]
        
        
# @lc code=end