#
# @lc app=leetcode id=120 lang='python3'
#
# [120] Triangle
#

# @lc code=start
from functools import cache
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        @cache
        def travel(y: int, x:int) -> int:
            if y == n - 1:
                return triangle[y][x]
            return triangle[y][x] + min(travel(y+1, x), travel(y+1, x+1))
        return travel(0,0)
# @lc code=end