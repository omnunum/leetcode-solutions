#
# @lc app=leetcode id=90 lang='python3'
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        subs = set()
        subs.add(tuple())
        for n in sorted(nums):
            subs |= {(n,) + s for s in subs}
        return subs
               
# @lc code=end