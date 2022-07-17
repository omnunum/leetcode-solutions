# @algorithm @lc id=198 lang=python3
# @title house-robber
from en.Python3.mod.preImport import *
class Solution:
    def rob(self, nums: list[int]) -> int:
        l2, l1 = 0, 0
        
        for n in nums:
            l2, l1 = l1, max(n + l2, l1)
        
        return l1
            