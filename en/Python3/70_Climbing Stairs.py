# @algorithm @lc id=70 lang=python3
# @title climbing-stairs
from en.Python3.mod.preImport import *
from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        # @cache
        # def num_ways_from(i: int) -> int:
        #     ways = 0
        #     if i == n:
        #         return 1
        #     if i < n:
        #         ways += num_ways_from(i+1)
        #     if i < n - 1:
        #         ways += num_ways_from(i+2)
        #     return ways
        # return num_ways_from(0)
        
#         # bottom up with O(n) space
#         dp = [1,2] + ([0] * (n - 2))
#         for i in range(2, n):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n-1]
    
        # bottom up with O(1) space
        pp, p = 1, 1
        for _ in range(1, n):
           pp, p = p, pp + p
        return p
        