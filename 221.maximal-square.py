#
# @lc app=leetcode id=221 lang='python3'
#
# [221] Maximal Square
#

# @lc code=start
from functools import cache
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
#         # Top down recursion and memoization
#         @cache
#         def traverse(y: int, x: int) -> int:
#             if (val := matrix[y][x]) == "0" or y == m-1 or x == n-1:
#                 return int(val)
#             right = traverse(y, x+1)
#             down = traverse(y+1, x)
#             cross = traverse(y+1, x+1)
#             return min(right, down, cross) + 1
        
#         maxed = 0
#         for y in range(m):
#             for x in range(n):
#                 maxed = max(maxed, traverse(y,x))
#         return maxed**2


        # # Bottom up iteration
        # maxed = 0
        # dp = [[None] * n for _ in range(m)]
        # for y in range(m-1, -1, -1):
        #     for x in range(n-1, -1, -1):
        #         val = matrix[y][x]
        #         if val == "0" or y == m-1 or x == n-1:
        #             dp[y][x] = int(val)
        #         else:
        #             right = dp[y][x+1]
        #             down = dp[y+1][x]
        #             cross = dp[y+1][x+1]
        #             dp[y][x] = min(right, down, cross) + 1
        #         maxed = max(maxed, dp[y][x])
        # return maxed ** 2
        
        # Bottom up iteration with O(N) memory
        maxed = 0
        dp = [[None] * n for _ in range(2)]
        for y in range(m-1, -1, -1):
            for x in range(n-1, -1, -1):
                val = matrix[y][x]
                if val == "0" or y == m-1 or x == n-1:
                    dp[0][x] = int(val)
                else:
                    right = dp[0][x+1]
                    down = dp[1][x]
                    cross = dp[1][x+1]
                    dp[0][x] = min(right, down, cross) + 1
                maxed = max(maxed, dp[0][x])
            dp[0], dp[1] = [None] * n, dp[0]
        return maxed ** 2
# @lc code=end