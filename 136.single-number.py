
#
# @lc app=leetcode id=136 lang='python3'
#
# [136] Single Number
#

# @lc code=start
        
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        found = 0
        for n in nums:
            found ^= n
        return found
# @lc code=end