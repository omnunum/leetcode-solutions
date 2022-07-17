# @algorithm @lc id=46 lang=python3
# @title permutations
from en.Python3.mod.preImport import *
from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return permutations(nums, len(nums))