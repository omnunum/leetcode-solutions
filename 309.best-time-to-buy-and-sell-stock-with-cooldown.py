#
# @lc app=leetcode id=309 lang='python3'
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
from dataclasses import dataclass
@dataclass
class State:
    bought: int
    cooled: int
    sold: int

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        curr = State(float("-inf"), 0, 0)
        for p in prices:
            prev = State(curr.bought, curr.cooled, curr.sold)
            # can either do nothing or cool from the sold state
            curr.cooled = max(prev.cooled, prev.sold)
            # can either do nothing or buy against the cooled state
            curr.bought = max(prev.bought, prev.cooled - p)
            # can sell by adding the price to the bought profit
            curr.sold = prev.bought + p
        return max(curr.bought, curr.cooled, curr.sold)
# @lc code=end