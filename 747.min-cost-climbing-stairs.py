
#
# @lc app=leetcode id=747 lang='python3'
#
# [747] Min Cost Climbing Stairs
#

# @lc code=start
        
from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @lru_cache
        def find_cost(s: int):
            cs = cost[s] if s >= 0 else 0
            
            if s+2 < len(cost):
                c = (find_cost(s+2), find_cost(s+1))
                return cs + min(c)
            
            return cs
        return find_cost(-1)
# @lc code=end