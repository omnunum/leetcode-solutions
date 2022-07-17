# @algorithm @lc id=213 lang=python3
# @title house-robber-ii
from en.Python3.mod.preImport import *
# S(i) = find the sum of the maximal path from house i to the last valid house
# S(i) = max(w(i) + S(i+2), w(i+1) + S(i+3))
# Boundary Case = S(-1) = w(-1), S(-2) = w(-2)
# T = 21m
from functools import cache
from collections import deque
class Solution:
    @cache
    def recurse(self, i: int, leave_early: bool) -> int:
        if i >= len(self.nums) - int(leave_early):
            return 0
        if i == len(self.nums) - 1 - int(leave_early):
            return self.nums[i]
        
        curr = self.nums[i] + self.recurse(i+2, leave_early)
        neighbor = self.nums[i+1] + self.recurse(i+3, leave_early)
        
        return max(curr, neighbor)
    
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        self.nums = nums
        neighbor = self.recurse(1, False)
        curr = self.recurse(0, True)
        return max(neighbor, curr)

        
        
        