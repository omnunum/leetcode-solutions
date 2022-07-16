
#
# @lc app=leetcode id=1791 lang='python3'
#
# [1791] Richest Customer Wealth
#

# @lc code=start
        
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(w) for w in accounts])
# @lc code=end