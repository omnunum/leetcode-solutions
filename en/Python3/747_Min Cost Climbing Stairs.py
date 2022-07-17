# @algorithm @lc id=747 lang=python3
# @title min-cost-climbing-stairs
from en.Python3.mod.preImport import *
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