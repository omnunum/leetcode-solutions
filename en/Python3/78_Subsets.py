# @algorithm @lc id=78 lang=python3
# @title subsets
from en.Python3.mod.preImport import *
# from itertools import chain, combinations
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # combs = (combinations(nums, i) for i in range(len(nums)+1))
        # return list(chain.from_iterable(combs))

        subs = [[]]
        
        for n in nums:
            for i in range(len(subs)):
                subs.append(subs[i] + [n])
        return subs