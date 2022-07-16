
#
# @lc app=leetcode id=152 lang='python3'
#
# [152] Maximum Product Subarray
#

# @lc code=start
        
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_local = float("inf")
        max_local = float("-inf")
        max_global = max_local
        
        for n in nums:
            if n < 0:
                min_local, max_local = max_local, min_local
            min_local = min(n, min_local * n)
            max_local = max(n, max_local * n) 
            max_global = max(max_local, max_global)
        return max_global
        
        
# @lc code=end