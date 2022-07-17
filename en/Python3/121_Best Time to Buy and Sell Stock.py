# @algorithm @lc id=121 lang=python3
# @title best-time-to-buy-and-sell-stock
from en.Python3.mod.preImport import *
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low, maxi = float("inf"), 0
        for p in prices:
            if p < low:
                low = p
            if (d := p - low) > maxi:
                maxi = d
        return maxi