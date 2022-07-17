# @algorithm @lc id=494 lang=python3
# @title target-sum
from en.Python3.mod.preImport import *
class Solution:
  def findTargetSumWays(self, nums, target):
    dp = defaultdict(int)
    dp[0] = 1


    for num in nums:
        new_dp = defaultdict(int)
        for n in dp:
            new_dp[n+num] += dp[n]
            new_dp[n-num] += dp[n]

        dp = new_dp


    return dp[target]