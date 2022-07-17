# @algorithm @lc id=128 lang=python3
# @title longest-consecutive-sequence
from en.Python3.mod.preImport import *
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        match len(nums):
            case 0: return 0
            case 1: return 1
        
        max_len = 1
        nums.sort()
        prev, curr_len = nums[0], 1
        for n in nums[1:]:
            if n == prev + 1:
                curr_len += 1
                max_len = max(curr_len, max_len)
            elif n == prev:
                continue
            else:
                curr_len = 1
            prev = n
        return max_len