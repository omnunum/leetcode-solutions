
#
# @lc app=leetcode id=198 lang='python3'
#
# [198] House Robber
#

# @lc code=start
        
class Solution:
    def rob(self, nums: list[int]) -> int:
        l2, l1 = 0, 0
        
        for n in nums:
            l2, l1 = l1, max(n + l2, l1)
        
        return l1
            
# @lc code=end