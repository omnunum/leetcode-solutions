# @algorithm @lc id=45 lang=python3 
# @title jump-game-ii
from en.Python3.mod.preImport import *
# @test([2,3,1,1,4])=2
# @test([2,3,0,1,4])=2
# @test([0])=0
# @test([2,1])=1
from functools import cache
class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     '''naive memoized brute force'''
    #     n = len(nums)
    #
    #     @cache
    #     def go(i: int) -> int:
    #         if i >= n-1:
    #             return 0
    #         min_downstream = float("inf")
    #         for step in range(nums[i], 0, -1):
    #             min_downstream = min(min_downstream, go(i+step))
    #         return min_downstream + 1
    #
    #     return go(0)
    def jump(self, nums: List[int]) -> int:
        '''bottom up dynamic programming'''
        n = len(nums)
        dp = [float("inf") for _ in range(n)]
        dp[-1] = 0
        for i in range(n-2, -1, -1):
            jump = nums[i]
            if not jump:
                continue
            if i + jump > n-1:
                dp[i] = 1
                continue
            dp[i] = min(dp[i+1:i+1+jump]) + 1
        return dp[0]
