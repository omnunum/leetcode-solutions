# @algorithm @lc id=136 lang=python3
# @title single-number
from en.Python3.mod.preImport import *
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        found = 0
        for n in nums:
            found ^= n
        return found