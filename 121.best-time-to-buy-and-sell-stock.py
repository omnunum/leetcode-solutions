
#
# @lc app=leetcode id=121 lang='python3'
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
        
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low, maxi = float("inf"), 0
        for p in prices:
            if p < low:
                low = p
            if (d := p - low) > maxi:
                maxi = d
        return maxi
# @lc code=end