#
# @lc app=leetcode id=46 lang='python3'
#
# [46] Permutations
#

# @lc code=start
from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return permutations(nums, len(nums))
# @lc code=end