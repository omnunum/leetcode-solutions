
#
# @lc app=leetcode id=64 lang='python3'
#
# [64] Minimum Path Sum
#

# @lc code=start
        
from functools import cache
class Solution:
    
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
#         # top down recursive
#         @cache
#         def traverse(y: int, x: int) -> int:
#             if y == m-1 and x == n-1:
#                 return grid[y][x]
#             # if we're at the bottom edge only move right
#             if y == m-1:
#                 return grid[y][x] + traverse(y, x+1)
#             # if we're at the right edge only move down
#             elif x == n-1:
#                 return grid[y][x] + traverse(y+1, x)
#             # otherwise return the min of either right or down move
#             return min(
#                 grid[y][x] + traverse(y+1, x),
#                 grid[y][x] + traverse(y, x+1)
#             )
        
#         return traverse(0,0)
        # Bottom up iterative
        dp = [[0] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                g = grid[y][x]
                # Base case
                if (y,x) == (0,0):
                    dp[y][x] = g
                    continue
                if y == 0:
                    dp[y][x] = g + dp[y][x-1]
                elif x == 0:
                    dp[y][x] = g + dp[y-1][x]
                else:
                    dp[y][x] = min(
                        g + dp[y][x-1],
                        g + dp[y-1][x]
                    )
        return dp[m-1][n-1]
                    
    
        
    
    
# @lc code=end