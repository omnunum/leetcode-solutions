# @algorithm @lc id=256 lang=python3
# @title paint-house
from en.Python3.mod.preImport import *
# goal: minimize cost of painting houses such that no adjacent houses have the same paint color
# S(n) = min(c[i]) + S(i+1)
# costs = [[3,2,17],[5,3,17],[6,3,5]]
class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        # min values per color
        rm, gm, bm = costs[0]
        for (r, g, b) in costs[1:]:
            rm, gm, bm = r + min(gm, bm), g + min(rm, bm), b + min(rm, gm)
        return min(rm, gm, bm)