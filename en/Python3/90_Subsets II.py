# @algorithm @lc id=90 lang=python3
# @title subsets-ii
from en.Python3.mod.preImport import *
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        subs = set()
        subs.add(tuple())
        for n in sorted(nums):
            subs |= {(n,) + s for s in subs}
        return subs
               