# @algorithm @lc id=96 lang=python3
# @title unique-binary-search-trees
from en.Python3.mod.preImport import *
from functools import cache
class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def ways_to_build(nums: tuple) -> int:
            if len(nums) <= 1:
                return 1
            ways = 0
            for i, n in enumerate(nums):
                left, right = nums[:i], nums[i+1:]
                ways += ways_to_build(left) * ways_to_build(right)
            return ways
        return ways_to_build(tuple(range(n)))