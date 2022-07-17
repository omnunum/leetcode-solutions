# @algorithm @lc id=265 lang=python3
# @title paint-house-ii
from en.Python3.mod.preImport import *
class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        dp = costs[0]
        for house in costs[1:]:
            dp = [
                cost + min(dp[:i] + dp[i+1:]) 
                for i, cost in enumerate(house)
            ]
        return min(dp)